class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:

        seen = set()

        for email in emails: 
            local, domain = email.split("@")
            local = local.split("+")[0] # when we see + keep the 1st portion
            local = local.replace(".", "") # when we see "." replace it with nothing
            seen.add(local + "@" + domain)

        return len(seen)