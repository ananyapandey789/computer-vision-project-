# Use Case Diagram

```mermaid
usecaseDiagram
    actor User
    actor System

    User --> (Run Pipeline)
    User --> (Provide Input Images)
    User --> (View Output Report)

    (Run Pipeline) .> (Preprocess Image) : includes
    (Run Pipeline) .> (Detect Objects) : includes
    (Run Pipeline) .> (Detect Faces) : includes
    (Run Pipeline) .> (Analyze Metrics) : includes
    (Run Pipeline) .> (Generate Report) : includes
```
