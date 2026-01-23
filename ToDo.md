### Firebase Web API Key
- GitHub and Google incorrectly flag this key as a leaked secret and send security alert emails.
- Firebase Web API keys are not secrets, they only identify which Firebase project to talk to.
- Google documentation states "API keys for Firebase services are OK to include in code or checked-in config files." See https://firebase.google.com/docs/projects/api-keys
- In addition, to prevent brute force attacks or infinite loop type of problems, I restricted domains and quota in Google Cloud Console.
    -- Applications restricted to my github pages website and localhost. When testing is done localhost can also be removed in Google Cloud Console -> APIs & Services -> Credentials -> BrowserKey -> Key Restrictions
    -- API can be restricted to Identity Toolkit API in the same place
    -- I looked into quota restriction under APIs & Services -> Enabled APIs & services -> Identity Toolkit API -> Quotas. It does not allow to set quota. Need to look into billing and budget alert and possibly some additional monitoring.
- If GitHub continues to alert, look into github/secret_scanning.yml as a way to supress false positive scanning alerts.