# uptime

A simple uptime monitor written in Python and HTML. 

## How to use
-  Clone the repository
-  Update your websites in the `github/workflows/uptime-workflow.yml` in `Run uptime check and append data`
- Commit the changes and push to the repository
- After first workflow run, go to Repository Settings &rarr; Pages &rarr; Build and Deployment and select the `gh-pages` branch and `/root` folder.
- Go to the link provided in the Pages section to see the uptime monitor.

> [!TIP]
> Change the interval of the uptime check by changing the cron schedule in the `github/workflows/uptime-workflow.yml`
  

## Acknowledgements
Based on AnandChowdhary's [uptime](https://github.com/upptime/upptime) project.


Thanks to ClaudeAI for the HTML :)
