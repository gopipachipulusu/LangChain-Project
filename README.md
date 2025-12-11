# 🌟 LangChain LLM Project

A hands-on project showcasing my ability to build intelligent workflows using LangChain, OpenAI, Agents, and Memory.

## 📌 Project Overview

This project demonstrates my practical experience working with LangChain, Large Language Models, and tool-augmented AI pipelines.
I built this project end-to-end to understand how LLMs work in real-world scenarios, how prompts can be structured, and how multi-step AI workflows can be automated.

The code includes various LangChain components such as LLMs, Prompt Templates, Chains, Agents, and Memory — all integrated to show how AI systems can perform reasoning, tool usage, and conversational continuity.

## 🎯 What This Project Demonstrates

This project reflects my ability to:

✔ Work directly with OpenAI LLMs

- Configure models

- Generate predictions

- Control temperature and output behavior

✔ Build reusable and dynamic prompts

- Using PromptTemplate, I created structured prompts that accept variables (like cuisine types) to generate restaurant names and menu items.

✔ Create LLM Chains & Multi-Step Pipelines

- I built multiple kinds of chains:

- LLMChain – basic chain with templates

- SimpleSequentialChain – flows output → input

- SequentialChain – more advanced chain with named inputs/outputs

Example pipeline I implemented:

Step 1: Generate a restaurant name

Step 2: Generate menu items for that restaurant

✔ Implement Agents with external tools

- I integrated Agents using:

- SerpAPI → for online search

- Wikipedia → for factual lookup

- LLM-Math → for numerical reasoning

- I built agent examples that:

- Search GDP values, then perform math

- Retrieve information (e.g., Elon Musk’s birth year) and compute age

- This demonstrates tool-use, reasoning, and agent action tracing.

✔ Add Memory to conversations

- I implemented multiple memory classes:

- ConversationBufferMemory – stores full conversation

- ConversationBufferWindowMemory – stores last k interactions

- ConversationChain – ready-made chat model with memory

- These examples show how previous inputs influence the conversation in real-time.

## 🧠 Skills Demonstrated

This project reflects my hands-on experience with:

LangChain Core Components

Prompt Engineering

LLM Reasoning Pipelines

Tool-Augmented AI Agents

Building AI workflows with memory

Working with external APIs

Structuring AI applications in Python

## 🛠 Tech Stack

Python

LangChain

OpenAI API

SerpAPI

Wikipedia Python Client

## 📂 Code Summary

The main script includes sections for:

Initializing LLMs

Prompt templates

LLM chains

Sequential chains

Agents with SerpAPI & Wikipedia

Conversation memory examples

I organized the code in a way that each component can be run independently for testing and learning.

## 🚀 Why I Built This

I created this project to strengthen my understanding of practical LLM development and to showcase my capability to:

Design AI-driven pipelines

Integrate external data sources

Create structured workflows

Build agentic reasoning systems

Implement memory-enabled chat agents

This project demonstrates my readiness for roles involving AI engineering, LLM integration, generative AI applications, and intelligent automation.

## 📌 Future Improvements

I plan to extend the project with:

RAG (Retrieval-Augmented Generation)

Vector databases (FAISS / ChromaDB)

Document question-answering pipelines

LangGraph-based agent workflows
