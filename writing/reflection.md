# Contact Searching

TO-DO: Make sure that you delete all of the TO-DO markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## Will Wolff

## Program Output

### What is the output from running the following commands?

```bash
- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`
```

```bash

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```bash
from contactsearcher import search
```

The source code above is asking to call the code within the file of contactsearcher and find and import the code of search and put it in the main code being used. The data needs the import in order for the output to be the desired one asked for. The imported data is used in the output by running the code for the data.

#### The source code statement that extracts the current job description for a contact
```bash

current_contact_job = contact_line[1]
        if job_description in current_contact_job.lower():
            list_contacts.append(contact_line)

```
TODO: Write at least one paragraph to explain the request source code

#### Invocation of the function called `search_for_email_given_job`

```bash

def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    list_contacts = []
    lines = csv.reader(contacts.splitlines(), delimiter=",", quotechar='"',
            quoting=csv.QUOTE_ALL, skipinitialspace=True,)
    for contact_line in lines:
        current_contact_job = contact_line[1]
        if job_description in current_contact_job.lower():
            list_contacts.append(contact_line)
    return list_contacts

```

TODO: Write at least one paragraph to explain the request source code

#### Test case for the function called `search_for_email_given_job`

```bash

============================= test session starts ==============================
platform darwin -- Python 3.10.6, pytest-7.1.1, pluggy-1.0.0
rootdir: /Users/willwolff/cs102/classDocs/08_survey_contact_searching-wolff01/contactsearcher
collected 5 items                                                              

tests/test_search.py .....

============================== 5 passed in 0.01s ===============================

```

TODO: Write at least one paragraph to explain the request source code

#### Execute trace of the `contactsearcher` program

TODO: Explain each function call that takes place for the following run of the program
TODO: Write at least one paragraph to explain every function call when running `contactsearcher`

TODO: Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.

### Based on your experiences with this project, what is one way in which you want to improve?

TODO: Provide a one-paragraph response that answers this question in your own words.
