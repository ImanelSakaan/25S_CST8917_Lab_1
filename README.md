# CST8917 Lab 1: Building Azure Function Apps with Output Bindings

## Objective

In this lab, you will develop two serverless Azure Function apps using **Python** and **Visual Studio Code**. You'll implement **output bindings** to connect your functions with Azure **Storage Queues** and **Azure SQL Database**.

You will complete the following official Microsoft QuickStart tutorials:

🔗 [Add an Azure Storage Queue output binding to a function in Azure](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?pivots=programming-language-python&tabs=isolated-process)  
🔗 [Add an Azure SQL output binding to a function in Azure](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-azure-sql-vs-code?pivots=programming-language-python)

By the end of this lab, you should understand how to configure output bindings and deploy function apps that push data to external services.

---

## About Azure Functions and Output Bindings

### What Are Azure Functions?

**Azure Functions** is a serverless compute service that enables you to run event-driven code without having to explicitly provision or manage infrastructure. Functions are triggered by events such as HTTP requests, queue messages, or database changes.

### What Are Output Bindings?

**Output bindings** simplify the way your functions interact with other Azure services by abstracting the logic required to connect and send data. This lets you focus on your app’s logic rather than service integration code.

For example, an output binding can:
- Send a message to a queue
- Write a record to a database
- Save a file to blob storage

---

## Tasks

### 1. Follow the Storage Queue Binding Tutorial

- Complete all steps from the [Storage Queue output binding QuickStart](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-storage-queue-vs-code?pivots=programming-language-python&tabs=isolated-process).
- Use Python as your programming language and VS Code as your development environment.
- Test the function locally and deploy it to Azure.
- Confirm that queue messages are added correctly when the function is triggered.

### 2. Follow the Azure SQL Binding Tutorial

- Complete all steps from the [Azure SQL output binding QuickStart](https://learn.microsoft.com/en-us/azure/azure-functions/functions-add-output-binding-azure-sql-vs-code?pivots=programming-language-python).
- Again, use Python and VS Code.
- Make sure to set up the Azure SQL Database and table schema as instructed.
- Verify that your function inserts records into the database successfully.

### 3. Documentation

Include a `README.md` with the following:

- Setup instructions for both functions, including any Azure resources you created (queues, databases).
- Steps to run and test the functions locally.
- A **5-minute demo video** showing:
  - Your function in action (queue message or database insert)
  - A quick walkthrough of your code and what you learned

### 5. GitHub Repository

- Use Git to track your work.
- Make **frequent, descriptive commits**.
- Push your project to a **public GitHub repository**.
- Include your **YouTube demo link in the README.md**.

---

## Submission Instructions

Submit your **GitHub repository link** via Brightspace.

**Deadline**: Thursday, 29 May 2025

---

## Tips

- Read each tutorial carefully and do not skip setup steps.
- Validate your code by reviewing the Azure Portal to confirm successful execution and output (queue or database).
- Ask for help early if you get stuck.
