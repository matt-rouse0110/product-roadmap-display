#Product Roadmap Display
##For end-users
This is intended to serve as a tool to easily convert a roadmap based in Jira into an externally communicatable format in PowerPoint.

It is executed as a downloadable .exe that will run on Windows without any dependencies.

The tool is designed to be flexible in terms of whether it uses a standardised JQL structure (`project = [project] and issuetype = "Epic" and resolution is empty`) or a completely bespoke JQL query, and also a flexible set of fields to extract. In the future, it will also accept an input file of issues that can be converted into a roadmap.

The tool will then extract the data, translate it into a roadmap format (after selecting the fields, you can then choose which fields are for content purposes and which ones drive phasing - currently only a single field for phasing is support). This format is then output into a powerpoint file, that you can then open and edit for any custom purposes.

The intent is to expedite the creation of roadmaps, such that the bulk of the heavy-lifting is automated and any minor alterations can be made manually.

If there are constant alterations needed, please feed these back, so that we can integrate these in as well.

##For developers
This tool is written in python and makes primary uses of tkinter, python-pptx and requests modules. 

For publishing purposes, a version of the code will be frozen and an executable produced via pyinstaller (refer to the [Spec file](./dataParser.spec) file)

Please reach out for any further guidance needed.