// super-linter reads stylelint.config.mjs from .github/linters; a
// .stylelintrc.json there is silently ignored.
export default {
  extends: ["stylelint-config-standard"],
  rules: {
    "no-descending-specificity": null,
    // Detection classes mirror the model's snake_case labels.
    "selector-class-pattern": null,
  },
};
