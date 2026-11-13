# Optional: route the offer letter to DocuSign

Only when the user chose DocuSign delivery. Needs a browser tool and a DocuSign account the user is already signed in to. Have the candidate's full name and email before opening the browser.

Use the browser tool to upload the offer letter into DocuSign and set up the
envelope, so the user doesn't have to touch DocuSign manually.

**Step-by-step browser flow:**

1. Navigate to `https://app.docusign.com` — the user should already be logged in.
   If a login screen appears, pause and ask the user to log in, then continue.

2. Click **"Start" → "Send an Envelope"** (or the equivalent "New" / "Use a Template"
   button depending on the UI version).

3. **Upload the offer letter:** Click "Upload Documents" and upload the
   `[Role]-Offer-Letter.docx` file that was just created.

4. **Add the signer:** In the Recipients section, add the candidate as a signer.
   Ask the user for the candidate's name and email if not already provided.
   Set their role to "Signer".

5. **Add the sender as a CC recipient** if the user wants a copy (ask if unsure).

6. **Set the subject line:** `Offer of Employment — [Role Title] at [Company Name]`

7. **Add a message:**
   > "Hi [Candidate First Name], we're thrilled to extend this offer and look
   > forward to having you join the team. Please review and sign at your
   > earliest convenience. Don't hesitate to reach out if you have any questions."

8. **Place signature fields:** On the document, place a Signature field and a
   Date Signed field on the candidate acceptance line at the bottom of the letter.

9. **Save as draft** — do NOT send. Return the envelope URL to the user so they
   can review before sending.

Tell the user:
> "The DocuSign envelope has been set up with the offer letter and candidate
> details. Here's the draft link: [ENVELOPE URL]. Review the signature placement,
> then confirm here when you're ready to send."

**Fallback:** If DocuSign is unavailable or the browser flow fails at any step,
fall back to the Gmail draft approach: draft an email with the connected email tool (if there is one), with the
offer letter attached and a note to upload it to DocuSign manually. Show the
draft to the user before sending.
