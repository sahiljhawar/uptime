# uptime

A simple uptime monitor written in Python and HTML. 

## How to use
### If using forked repository

- Fork the repository (you may choose to untick **Copy the `main` branch only**)
- Update your websites in the `github/workflows/uptime-workflow.yml` in `Run uptime check and append data`
- Commit the changes and push to the repository
- After that, go to the Actions tab and enable the workflow by clicking on the `I understand my workflows, go ahead and enable them` button.
- In the left sidebar, click on the `Check Websites Uptime and Deploy to GitHub Pages` and then click on the `Enable workflow` button to allow the scheduled workflows to run. Use `Run workflow` to run the workflow manually for the first time.
- Go to the link provided in the Pages section to see the uptime monitor.

### If using as template

- Click on the `Use this template` button to create a new repository from this template.
- Select `Include all branches`
- Give a name to the repository and click on the `Create repository from template` button.
- Update your websites in the `github/workflows/uptime-workflow.yml` in `Run uptime check and append data`
- Commit the changes and push to the repository

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
