class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        seen_emails = set()
        for email in emails: 
            local, domain = email.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            seen_emails.add(local + "@" + domain)
        return len(seen_emails)

        