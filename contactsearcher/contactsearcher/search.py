"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html 


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # TO-DO: create an empty list of the contacts
    list_contacts = []
    # TO-DO: iterate through the file, parsing it line by line
    read_contacts = r'/Users/willwolff/cs102/classDocs/08_survey_contact_searching-wolff01/contactsearcher/input/contacts.txt'
    # TO-DO: refer to the file called input/contacts.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse
    with open(read_contacts, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if job_description in reader:
                if contacts in reader:
                    list_contacts.append(row)
    return list_contacts
            
    # TO-DO: iterate through each line of the file and extract the current job
    # ---> TO-DO: extract the current job for the contact on this line of the CSV
    # ---> TO-DO: the job description matches and thus we should save it in the list
    # TO-DO: return the list of the contacts who have a job description that matches
