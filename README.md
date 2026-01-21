(Draft)

I need a better way to create homework for my language students. Google Classroom’s assignment tools are limited. For example, it is not possible to create interactive games or easily include graphics. Graded assignments are restricted to true/false, multiple choice, free-text responses.

Plan:

* Use the Google Classroom API to connect my website with Google Classroom.

* Host homework on my website, where students can submit their work; each submission will trigger a grade update in Google Classroom.

* Use Google Firebase Authentication so students can sign in with their Google accounts.

* Since Google only allows grade updates via the API from the same project that created the assignment, assignments will also need to be created via the API (script-based for now, no UI).