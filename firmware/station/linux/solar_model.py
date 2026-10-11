"""Sun position and clear-sky irradiance on a panel, in pure Python (no numpy/pvlib).

Models, chosen because they need only time, place and panel orientation:
- Sun position: NOAA solar calculator equations (Meeus-based), without
  atmospheric refraction; accurate to well under 0.1 deg for this purpose.
- Air mass: Kasten & Young (1989).
- Direct normal irradiance: Meinel & Meinel (1976), DNI = 1353 * 0.7^(AM^0.678).
- Diffuse: about 10 % of the direct beam (PVEducation rule of thumb), spread
  over the sky the panel sees (isotropic view factor (1 + cos tilt) / 2).

These give the irradiance expected on the panel under a clear sky. Clouds,
haze and shading lower the real value, so they look like soiling to anything
that compares against this model.
"""

import math

SOLAR_CONSTANT_WM2 = 1353.0


def sun_position(unix_s, lat_deg, lon_deg):
    """Return (elevation_deg, azimuth_deg) of the sun; azimuth clockwise from north."""
    jd = unix_s / 86400.0 + 2440587.5
    jc = (jd - 2451545.0) / 36525.0

    mean_long = (280.46646 + jc * (36000.76983 + jc * 0.0003032)) % 360
    mean_anom = 357.52911 + jc * (35999.05029 - 0.0001537 * jc)
    ecc = 0.016708634 - jc * (0.000042037 + 0.0000001267 * jc)
    m = math.radians(mean_anom)
    center = (
        math.sin(m) * (1.914602 - jc * (0.004817 + 0.000014 * jc))
        + math.sin(2 * m) * (0.019993 - 0.000101 * jc)
        + math.sin(3 * m) * 0.000289
    )
    omega = math.radians(125.04 - 1934.136 * jc)
    app_long = mean_long + center - 0.00569 - 0.00478 * math.sin(omega)
    mean_obliq = (
        23 + (26 + (21.448 - jc * (46.815 + jc * (0.00059 - jc * 0.001813))) / 60) / 60
    )
    obliq = math.radians(mean_obliq + 0.00256 * math.cos(omega))
    decl = math.asin(math.sin(obliq) * math.sin(math.radians(app_long)))

    y = math.tan(obliq / 2) ** 2
    l0 = math.radians(mean_long)
    eq_time_min = 4 * math.degrees(
        y * math.sin(2 * l0)
        - 2 * ecc * math.sin(m)
        + 4 * ecc * y * math.sin(m) * math.cos(2 * l0)
        - 0.5 * y * y * math.sin(4 * l0)
        - 1.25 * ecc * ecc * math.sin(2 * m)
    )

    minutes_utc = (unix_s % 86400) / 60.0
    true_solar_min = (minutes_utc + eq_time_min + 4 * lon_deg) % 1440
    hour_angle = math.radians(true_solar_min / 4 - 180)

    lat = math.radians(lat_deg)
    cos_zen = math.sin(lat) * math.sin(decl) + math.cos(lat) * math.cos(
        decl
    ) * math.cos(hour_angle)
    zen = math.acos(max(-1.0, min(1.0, cos_zen)))
    sin_zen = math.sin(zen)
    if sin_zen < 1e-9:
        azimuth = 180.0
    else:
        cos_az = (math.sin(lat) * math.cos(zen) - math.sin(decl)) / (
            math.cos(lat) * sin_zen
        )
        az = math.degrees(math.acos(max(-1.0, min(1.0, cos_az))))
        azimuth = (az + 180) % 360 if hour_angle > 0 else (540 - az) % 360
    return 90.0 - math.degrees(zen), azimuth


def air_mass(zenith_deg):
    """Relative optical air mass, Kasten & Young (1989); None below the horizon."""
    if zenith_deg >= 90:
        return None
    return 1.0 / (
        math.cos(math.radians(zenith_deg))
        + 0.50572 * (96.07995 - zenith_deg) ** -1.6364
    )


def clear_sky_poa(elevation_deg, azimuth_deg, tilt_deg, panel_azimuth_deg):
    """Expected clear-sky irradiance on the panel plane in W/m2 (0 at night)."""
    zenith = 90.0 - elevation_deg
    am = air_mass(zenith)
    if am is None:
        return 0.0
    dni = SOLAR_CONSTANT_WM2 * 0.7 ** (am**0.678)
    z, t = math.radians(zenith), math.radians(tilt_deg)
    cos_aoi = math.cos(z) * math.cos(t) + math.sin(z) * math.sin(t) * math.cos(
        math.radians(azimuth_deg - panel_azimuth_deg)
    )
    direct = dni * max(0.0, cos_aoi)
    diffuse = 0.1 * dni * (1 + math.cos(t)) / 2
    return direct + diffuse
