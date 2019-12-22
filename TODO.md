<!-- To view this file rendered, try opening VSCode and clicking to open the "Preview" pane -->
# TWIST - Project plan
Documenting the short-term and long-term development plan for the project. Of course, all of this is subject to change.

## Contents
<!-- This contents is kept up to date *manually* -->
1. [In development tasks](#In-development-tasks)
1. [Allocated to future releases](#Allocated-to-future-releases)
1. [Future wish list](#Future-wish-list)

<div align="right"><a href="#contents">Back to top</a></div>

## In development tasks
### v0.1.0: MVP Simulate and visualise two variables
- [x] Simulate two variables X_1,X_2 from joint normal with mean 0 and specified variances and covariance, using `numpy`. Specify number of points. Specify random seed.
- [x] Create class to hold simulated data + method to generate data + initialise with default values.
- [ ] Create dashboard app (separate module)
- [ ] Visualise scatter plot using `bokeh` package
- [ ] Visualise marginal histograms (e.g. <https://demo.bokeh.org/selection_histogram>)

<div align="right"><a href="#contents">Back to top</a></div>

## Allocated to future releases
### v0.2.0: MVP Simulate and visualise response
- [ ] Simulate response Y|X_1,X_2 variable from joint normal with mean mu = a_1 X_1 + a_2 X_2 + (a_3 - (a_1 + a_2))X_1 X_2 and specified (fixed) variance sigma^2.
- [ ] Visualise 3D scatter plot

### v0.3.0: MVP Interactive dashboard
- [ ] Add input widgets to dashboard and organise dashboard layout.

### v0.4.0: Save simulations and dashboard state
- [ ] Allow generated data to be saved and dashboard state to be restored.

### v0.5.0: MVP Fit linear model
- [ ] Use `sklearn` to fit the linear model with all variables. Create new class, which takes array object as input.
- [ ] Allow fit to be called with different parameters

### v0.6.0: MVP Fit model dashboard section
- [ ] Add section to dashboard for fitting the model, separate from simulator section.
- [ ] Print fit diagnostics to the dashboard. 
- [ ] Show true and fitted line of best fit between X_1,X_2
- [ ] Show true response plane and line, and fitted response line for Y

## Future wish list 
A brain-dump of all possible desirable features, grouped by topic, *not* by priority. Select from these to put into future releases.
- Dashboard:
    - Allow saving state / data
- Simulations
    - Allow X_2 explanatory variable to be discrete. 
        - Specify number of levels (start with 2)
        - Specify effective value along the X_2 axis (start with one at each extreme)
        - Appropriate visualisation, e.g. marginal histograms and/or scatter plot with jitter, points coloured by level
- Fitting:
    - Linear model:
        - Hypothesis tests for which variables are statistically significant. Specify significance level.
    - GBM (e.g. `xgboost`):
        - Fit (e.g. with some default parameters)
        - Visualise
        - Splint data by training-test. Fit on training, visualise on both.
        - Allow hyperparameter tuning, e.g. grid search.
- Code structure:
    - Add automated tests and allow them to easily be run
    - Convert code to a Python package
    - Automate build using CI software (e.g. Azure DevOps 'Pipelines')
    - Deploy package to an online package host (e.g. using Azure DevOps 'Artifacts')
    - Host the dashboard as an app on some service (e.g. Heroku)
- Documentation:
    - Additions to README:
        - Summarise the purpose of the project including screenshots 
        - Clear disclaimer for project
    - Allow mathematical notation in docs (e.g. by switching from markdown to Rmarkdown).
    - Set up automated creation of documentation from docstrings
    - Automate documentation of the project structure (instead of keeping it in a manual `.md` file)
    - Write a notebook giving example usage of the project
- Promotion:
    - Blog post (e.g. on Medium) giving examples
    - Blog post about how the code was developed
    - Post to social media channels: LinkedIn (+ more?)
- Project management
    - Move TODO list to automated management (e.g. GitHub Issues or Azure DevOps 'Boards') both features (aka "milestones" and tasks (aka "issues")

<div align="right"><a href="#contents">Back to top</a></div>
