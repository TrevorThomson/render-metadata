Render Metadata
===============
A sandbox for experimenting with distributed services and data base

Design
------
Note: we're focusing on a functional toy system, not on production-level completeness.

Render Service
 - api layer
 - model layer
 - data access layer

API
- create a Shot
    - note: we're implementing this in the Render Service API for simplicity
- queue a render given a Shot name
- check status of a render given a Shot name

Model
- Renderer
- Shot
    - shot id
    - list of frames
- Frame
    - frame number
    - render status

Data Access
- Store new Shot
- Update Shot (e.g. frame status)
- Read Shot
- tables:
    - Shots
    - Frames
        - primary key: shotID + frameNumber
