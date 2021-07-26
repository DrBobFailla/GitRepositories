__author__ = "Bob Failla"
__purpose__ = "Print a list of unique senders from a file, obstensibly an mbox file"
__description__ = "First used after importing my Protonmail inbox since it doesn't allow sorting by sender." \
                  "Sorting by sender allows a faster removal of email it's not necessary to keep.  Next run on" \
                  "the spam folder to ensure there are no valid senders trapped in there before deleting."

if __name__ == "__main__":
    filename = "/Users/Bob/Spam.mbox"
    with open (filename, "r") as inboxhandle:
        mailbox = inboxhandle.readlines()
        senders = {x for x in mailbox if "From: \"" in x} # This comprehension generates a list of senders.

    for i in sorted(senders):
        print(i.replace("From: ", ""), end="")
    print(len(senders))