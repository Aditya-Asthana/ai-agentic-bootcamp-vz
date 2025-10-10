# Verizon / IBM Langflow Workshop  
**Accelerating AI-Powered Support and Knowledge Systems in Telecommunications**

---

## Overview

This workshop introduces developers to the foundational concepts of **Langflow**, showing how it can be used to create intelligent, data-driven assistants within a realistic telecom scenario. Coupled with the abilities of **watsonx Orchestrate**, Verizon has a complete source for agentic and RAG based AI development, deployment, and monitoring.

In this fictional story, Verizon’s internal technology innovation team is exploring how to modernize its customer support systems using IBM’s suite of AI tools. Through a series of guided exercises, participants will use Langflow—an open-source visual orchestration platform—to design, test, and deploy flows that combine **large language models (LLMs)**, **vector search**, and **agentic reasoning** to power next-generation support tools.  

By the end of the workshop, you will have created working prototypes that demonstrate how telecom organizations can leverage AI to unify internal knowledge, improve customer experiences, and streamline employee workflows.

---

## Business Context

Verizon’s support operations rely on large volumes of documentation, ranging from device manuals and network troubleshooting guides to account policies and promotional terms. Over time, these sources of information have grown fragmented, making it difficult for employees and digital agents to quickly retrieve the right information.  

To address this, Verizon’s internal AI Innovation team—working with IBM—has begun piloting a unified knowledge system built on **Langflow**, **IBM watsonx.ai**, and **DataStax Astra DB**. The goal: to turn this distributed knowledge into a searchable, conversational system that can reason about questions, retrieve the right context, and provide accurate answers instantly.  

In this workshop, Langflow acts as the orchestration layer—visually connecting IBM’s models and services with Astra DB’s vector database to build intelligent agents step by step.

---

## Workshop Objectives

By completing this workshop, you will learn how to:

- Build and configure AI-powered flows using **Langflow** and **IBM watsonx.ai**.  
- Connect to a **vector-enabled Astra DB** to store and retrieve knowledge documents.  
- Create your own **retrieval-augmented generation (RAG)** pipelines.  
- Use **agentic design patterns** to let AI assistants call specialized tools.  
- Experiment with **multi-agent orchestration** for complex telecom use cases.  

The exercises build on each other—each one adding a new layer of intelligence, automation, or data connectivity.

---

## Technical Prerequisites

Before beginning, ensure that you have the following configured:

- A **DataStax Astra DB Vector** instance (serverless, AWS us-east-2 region).  
- An **Astra DB application token** with read/write privileges.  
- An **IBM watsonx.ai project** and API key.  
- **Langflow Desktop** or **OSS Langflow** installed locally.  
- The ability to create **Global Variables** inside Langflow for API credentials.  

Workshop facilitators will provide guidance and verification before exercises begin.

---

## Workshop Exercises Overview

The workshop is organized into six exercises. Each builds on the previous one to create a fully functional multi-agent retrieval system.

---

### Exercise 1: Hello World Chatbot

In this first exercise, you’ll create a simple chatbot flow that connects **Langflow** to **IBM watsonx.ai**.  
This establishes basic connectivity and helps confirm your API and model credentials are working correctly.  

Participants will:
- Create a new blank flow.  
- Add and connect Chat Input, IBM watsonx.ai, and Chat Output components.  
- Test interaction in Langflow’s Playground interface.  

**Outcome:**  
A working LLM chatbot capable of responding to basic questions—the foundation for all subsequent flows.

---

### Exercise 2: Enriched RAG Ingest

Next, you’ll learn how to **ingest and enrich documents** before storing them in a vector database.  
Using Langflow’s Batch Run, Split Text, and DataFrame components, you will categorize, summarize, and keyword-tag PDF files before inserting them into Astra DB.

Participants will:
- Load a dataset of internal Verizon documentation.  
- Extract categories and summaries using IBM watsonx.ai.  
- Generate embeddings with watsonx.ai Embeddings.  
- Store enriched data in Astra DB for semantic retrieval.

**Outcome:**  
A structured, searchable knowledge base that supports retrieval-augmented generation.

---

### Exercise 3: Enriched RAG Retriever Flow

Building on the previous step, this exercise demonstrates how to **retrieve and reason** over stored knowledge.  

Participants will:
- Create a flow that uses Astra DB as a vector retriever.  
- Use watsonx.ai to generate query embeddings and context-aware responses.  
- Parse and prompt results using Langflow components.  

**Outcome:**  
A question-answering system capable of returning accurate, context-driven responses based on stored Verizon documents.

---

### Exercise 4: Agentic Flow with Tool Calling

This exercise introduces **agentic reasoning**—enabling your AI to decide which tool or database to use when responding.  

Participants will:
- Create an **Agent component** that coordinates multiple Astra DB tools.  
- Configure specialized search endpoints for *Promotions*, *System and Tools*, and *Account Support*.  
- Use watsonx.ai as the reasoning model and IBM Embeddings for search vectorization.  

**Outcome:**  
An intelligent assistant that can automatically select the most relevant dataset to answer user questions—a critical step toward production-ready support bots.

---

### Exercise 5: Agent RAG Retriever Flow

Now you’ll integrate the **Agent** into your **retriever flow**, enabling the model to combine reasoning with knowledge retrieval.  

Participants will:
- Link the Tool Calling Agent created earlier into a new retriever flow.  
- Replace direct database queries with an agent call.  
- Test responses that blend retrieval accuracy with contextual understanding.  

**Outcome:**  
A unified, intelligent flow capable of both finding and explaining information from multiple domains.

---

### Exercise 6: Multi-Agent Flow with MCP Tool

In this final exercise, you’ll create a **multi-agent system** that leverages tool orchestration through Langflow’s **MCP integration**.  

Participants will:
- Configure an MCP Tool Server inside Langflow.  
- Combine the Agent RAG Retriever and a Calculator tool into a coordinated multi-agent flow.  
- Demonstrate complex reasoning with real-time calculations and document citations.  

**Outcome:**  
A flexible, modular agent system capable of handling advanced support scenarios—such as billing, troubleshooting, and promotional analysis.

---

## Architecture Overview

The workshop architecture is composed of three core layers:

| Layer | Purpose | Tools & Components |
|-------|----------|--------------------|
| **Foundation** | Data and vector storage | DataStax Astra DB |
| **Cognitive** | Model reasoning and embeddings | IBM watsonx.ai, IBM Embeddings |
| **Orchestration** | Flow design, tool management, and interaction | Langflow |

Langflow visually connects these services, allowing developers to rapidly prototype, debug, and iterate on AI workflows without extensive code.  
Each exercise progressively deepens the integration between these layers—from simple model calls to fully orchestrated multi-agent reasoning.

---

## Workshop Flow Summary

| Module | Key Capability | Business Value |
|---------|----------------|----------------|
| Hello World Chatbot | LLM basics | Demonstrates conversational AI potential |
| Enriched RAG Ingest | Knowledge base creation | Enables context-driven answers |
| RAG Retriever Flow | Contextual retrieval | Empowers agents with verified content |
| Agentic Flow | Tool selection & routing | Increases response accuracy |
| Agent RAG Retriever | Combined retrieval + reasoning | Reduces manual support effort |
| Multi-Agent Flow | Cooperative agents & tools | Models complex telecom scenarios |

---

## Next Steps

After completing the exercises, participants are encouraged to:

- Extend Langflow flows to include additional IBM services such as **watsonx.governance** or **watsonx.data**.  
- Explore deployment strategies using containerized runtimes or edge integrations.  
- Adapt the fictional Verizon scenario to internal proof-of-concept projects.  

---

## Conclusion

Through this hands-on workshop, developers experience how **Langflow**, **IBM watsonx.ai**, and **Astra DB** together can transform raw documentation into actionable intelligence.  

By the end, you’ll not only understand how to connect the components—you’ll see how to translate AI-powered workflows into real-world business impact across customer service, operations, and product support within a modern telecommunications environment.

