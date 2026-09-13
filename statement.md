# Project Statement: SubTrack — Subscription Management System

## Problem Statement
Most people sign up for multiple recurring subscriptions — streaming, cloud storage, software tools — and lose track of them over time. Without a single place to see everything, it's easy to miss a renewal date or get charged for something you forgot you were still paying for.

## Scope of the Project
SubTrack is a Python command-line application that lets a user manage their recurring subscriptions from one place: adding, viewing, and removing them, and checking their total monthly and yearly spend. All data is stored locally in a JSON file, so there's no external database or setup required beyond running the script.

## Target Users
- Individuals who want a simple way to track their monthly and yearly subscription costs
- Budget-conscious users who want a clearer picture of their recurring expenses

## High-Level Features
1. Add, view, and delete subscriptions, each with a cost, billing cycle, category, and renewal date
2. Automatic calculation of total monthly and yearly subscription spend
3. Persistent local storage using JSON, so data isn't lost between sessions
4. Basic input validation (e.g. rejecting non-numeric cost values) to prevent the program from crashing on bad input