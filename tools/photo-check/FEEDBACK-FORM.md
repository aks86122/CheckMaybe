# Public feedback: Google Form (founder decision 2026-10-25)

Why: public-link visitors can't write to the artifact database (see SECURITY-REVIEW.md, risk 1). The page will open a Google Form in a new tab with the answers and the check's findings already filled in; the visitor presses Submit on Google's page.

## Form to create (founder, in Google Forms)
Title: CheckMaybe Photo Check feedback
Description: Tell us if the photo check got it right. Don't include names, contact details or anything private.

| # | Question | Type | Required | Options |
| --- | --- | --- | --- | --- |
| 1 | Was this result right? | Multiple choice | Yes | Yes / No |
| 2 | What is it really? | Dropdown | No | A straight-from-camera photo / An edited photo / Made with AI / A photo edited with AI / A screenshot / Someone else's image / A design or mockup (not a photo) / Not sure |
| 3 | App or AI tool used | Short answer | No | |
| 4 | Anything else we should know? | Paragraph | No | |
| 5 | Check details (filled in by the tool, please don't edit) | Paragraph | No | |

Settings: Collect email addresses = Do not collect; "Restrict to users in ..." off; "Limit to 1 response" off (so no Google sign-in is needed). Responses: link to a new Google Sheet.

## Wiring
Founder sends the pre-filled link (⋮ menu → Get pre-filled link, fill every question with any answer, Get link). The `entry.<number>` ids in that link go into the page. Field 5 carries the same findings the database rows had (verdict, signals, format, size, flags, source types, tools, file-name pattern, tool version), as one line of JSON. The form URL is opened only when the visitor presses Send; nothing is sent in the background.

## Done (2026-10-25)
Form created by the founder (anonymous, no sign-in needed; Q1 also has "Maybe"). Entry ids read from the public form page: right 1031372084, actual 2118168332, tool 920764767, comment 1367118987, check 1662659418. "Send feedback" is now a link that opens the form pre-filled (tested: all five fields filled, URL about 800 characters); the visitor presses Submit. The page no longer writes to the artifact database; the 2 earlier rows stay there. Not submitted in testing, so the response sheet has no test row.

Fix (same day): the founder's first test response had Q5 empty. Likely cause: the claude.ai viewer opens a clicked link with the address it had before the page's click handler ran, so it opened the bare form. The link's address is now updated on every answer change, before any click.

Response sheet (owner qwert900823, shared with the connector account): 1eove0DVWPGdb1tz7Q-EMDNDz0eZ_u8e449ID2K8HN4g, tab 「表單回覆 1」. First pre-filled row arrived 2026-10-25 16:42 with Check details filled, so the fix works.
