# CST8917 Lab 1: Building Azure Function Apps with Output Bindings
---
🎥 Demo Video

YouTube Demo Link - 5 Minute Walkthrough
https://youtu.be/LposiZiC8v4

# Lab: Serverless Azure Functions with Output Bindings

Serverless is a development model that allows developers to build and run applications without having to manage servers. There are still servers in serverless, but they are abstracted away from app development.

This lab involves creating two serverless functions with output bindings:
- One for **Azure Storage Queues**
- One for **Azure SQL Database**

---

## Prerequisites

### 1. Install Required Tools

- [Visual Studio Code with Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
- Python 3.8 or higher
- [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Git](https://git-scm.com/)
- Active Azure subscription

---

### 2. Check Installation

#### ✅ Check Azure Functions Core Tools

    func --version
    4.0.7317

#### ✅ Check Azure CLI
    az --version
    
    azure-cli    
    2.70.0 *

#### ✅ Check Azure Subscription
    az account list --output table

### 3. Install VS Code Extensions
    Azure Functions extension
    Python extension

### 4. Sign in to Azure
    az login

---
# Part 1: Azure Storage Queue Output Binding / HTTP Trigger

Let's start with the first tutorial – adding a Storage Queue output binding.

---

## Step 1: Create the Function Project

### 1. Create a new folder for your project:

mkdir azure-functions-lab
cd azure-functions-lab

### 2. Initialize the Function project in VS Code

- Open VS Code in the current directory: `code .`
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
- Type **"Azure Functions: Create New Project"**
- Select the current folder
- Choose **"Python"** as the language
- Choose **"Python 3.8+"** as the Python interpreter
- Select **"HTTP trigger"** as the template
- Name your function **"SendToQueue"**
- Choose **"Function"** for authorization level

  ## Step 2: Add Storage Queue Output Binding

1. Modify the `function.json` file  
   *(this should be auto-generated in the `HttpExample` folder)*

2. Update the Python function code in:  
   `HttpExample/__init__.py`

---

## Step 3: Test the Function

### Start the function locally

func start

### Test URLs

- [http://localhost:7071/api/SendToQueue](http://localhost:7071/api/SendToQueue)
- [http://localhost:7071/api/SendToQueue?name=Azure](http://localhost:7071/api/SendToQueue?name=Azure)


---

# Create supporting Azure resources for your function

Before you can deploy your function code to Azure, you need to create three resources:

1. **A resource group**, which is a logical container for related resources.
az group create --name AzureFunctionsQuickstart-rg --location canadacentral

2. **A Storage Account**
A storage account, which maintains the state and other information about your projects.
az storage account create --name azurestoragename123 --location canadacentral --resource-group AzureFunctionsQuickstart-rg --sku Standard_LRS

## Create a Function App
Create a function app that provides the environment for executing your function code.
# Using Python 3.11.9 runtime, Windows OS
az functionapp create --resource-group AzureFunctionsQuickstart-rg --consumption-plan-location canadacentral --runtime python --runtime-version 3.11.9 --functions-version 4 --name http_trigger --os-type windows --storage-account azurestoragename123

## 4. Deploy to Azure
Deploy your function app to Azure using the Azure Functions Core Tools:
func azure functionapp publish http-trigger-app123

# Part 2: Azure SQL Output Binding / HTTP trigger with Azure SQL Database output binding

## Prerequisites
Install the Azure SQL extension for Azure CLI:
az extension add --name sql

1. **Create a New Azure Function**
Function name: **SqlOutputFunction2**

**Set Up Azure SQL Resources**
2. **Create a SQL Server:**
az sql server create --name lab1sqlserver123 --resource-group AzureFunctionsQuickstart-rg --location canadacentral --admin-user sqladmin --admin-password dodydody@100

2. **Create a SQL Database:**
az sql db create --resource-group AzureFunctionsQuickstart-rg --server lab1sqlserver123 --name Lab1Db --service-objective S0
















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
