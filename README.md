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
  

## To Do
- [ ] Add a way to notify when a website is down
- [ ] Add a way to notify when a website is up after being down for a while
- [ ] Add a way to notify when a website is down for a long time
- [x] Remove websites from JSON if they are removed from the workflow file

## Acknowledgements
Based on AnandChowdhary's [upptime](https://github.com/upptime/upptime) project.


Thanks to ClaudeAI for the HTML :)
