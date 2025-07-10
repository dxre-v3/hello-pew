# Pew Research Hello World Challenge

### Challenge
Build a GitHub Workflow that deploys a small "Hello World" JavaScript app, complete with Playwright tested, to ensure Hello World is rendered correctly. The workflow should handle tests, denying the deploy if the test failed, and sending an email to a group of users when complete.

Bonus Points:
- Send notifications to Slack API instead of email.
- Implement retry logic.

### Results
- The deployed app can be viewed at [https://dxre-v3.github.io/hello-pew](https://dxre-v3.github.io/hello-pew).
- Slack notifications can be viewed by [joining my test slack Allsis](https://join.slack.com/t/allsisworkspace/shared_invite/zt-399x19j80-rlAaP5kcxnp0lqpfQbL7ag) and viewing the `#pew-hello-challenge` channel.

#### Playwright Tests Details
- The Playwright test looks for an element with the id `hello-world`. Although this is an `H1` in my example, it does not have to be. 
- It then compares the text of the element to the expected string: `Hello World!`. If the string is not an exact match, the test will fail. 

#### Areas for Future Improvement
- Playwright browser installation is slow. It would be ideal to only install what is strictly necessary.
- The Playwright test could be more flexible, checking for the existance of the desired string instead of requiring an exact match. 
- Test_App would make a great reusuable workflow. 

### Sources Used: 

<details>
<summary>Expand for a (mostly) comprehensive list of resources used.</summary>

- [How to Install React – A Step-by-Step Guide](https://www.freecodecamp.org/news/how-to-install-react-a-step-by-step-guide/#heading-using-vite)
- [Animated Emoji](https://googlefonts.github.io/noto-emoji-animation/)
- [Implementing CI/CD pipeline with GitHub Actions, and GitHub Pages in a React app](https://dev.to/efkumah/implementing-cicd-pipeline-with-github-actions-and-github-pages-in-a-react-app-ij9)
- [Triggering a workflow](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)
- [How to add Playwright tests to your pull request CI with GitHub Actions](https://snyk.io/blog/how-to-add-playwright-tests-pr-ci-github-actions/)
- [How do I use Playwright to verify if a specific string is present in an h1 element?](https://ray.run/questions/how-do-i-use-playwright-to-verify-if-a-specific-string-is-present-in-an-h1-element)
- [Server Options](https://vite.dev/config/server-options)
- [Events that trigger workflows](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#workflow_run)
- [Using jobs in a workflow](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow)
- [Controlling Job Execution with Conditions in GitHub Actions](https://cicube.io/blog/github-actions-if-condition/)
- [Browsers | Playwright](https://playwright.dev/docs/browsers)
- [setup-python](https://github.com/actions/setup-python)
- [mailchimp-bots](https://github.com/CalMatters/mailchimp-bots)

</details>