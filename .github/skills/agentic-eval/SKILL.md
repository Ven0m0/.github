---
name: agentic-eval
description: |
  Patterns for evaluating and improving AI agent outputs. Use when implementing
  self-critique loops, evaluator-optimizer pipelines, test-driven code refinement,
  or rubric-based evaluation systems.
user-invocable: true
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Agentic Evaluation Patterns

Patterns for self-improvement through iterative evaluation and refinement.

```
Generate -> Evaluate -> Critique -> Refine -> Output
    ^                              |
    +------------------------------+
```

## When to Use

- Quality-critical generation (code, reports, analysis)
- Tasks with clear evaluation criteria
- Content requiring specific standards compliance

## Pattern 1: Basic Reflection

Agent evaluates and improves its own output through self-critique.

```python
def reflect_and_refine(task: str, criteria: list[str], max_iterations: int = 3) -> str:
    output = llm(f"Complete this task:\n{task}")
    for i in range(max_iterations):
        critique = llm(f"Evaluate against {criteria}. Output: {output}. Rate each: PASS/FAIL as JSON.")
        data = json.loads(critique)
        if all(c["status"] == "PASS" for c in data.values()):
            return output
        failed = {k: v["feedback"] for k, v in data.items() if v["status"] == "FAIL"}
        output = llm(f"Improve to address: {failed}\nOriginal: {output}")
    return output
```

## Pattern 2: Evaluator-Optimizer

Separate generation and evaluation into distinct components.

```python
class EvaluatorOptimizer:
    def run(self, task: str, threshold: float = 0.8, max_iter: int = 3) -> str:
        output = self.generate(task)
        for _ in range(max_iter):
            score = self.evaluate(output, task)
            if score["overall_score"] >= threshold:
                break
            output = self.optimize(output, score)
        return output
```

## Pattern 3: Test-Driven Code Refinement

```python
def reflect_and_fix(spec: str, max_iterations: int = 3) -> str:
    code = llm(f"Write Python code for: {spec}")
    tests = llm(f"Generate pytest tests for: {spec}\nCode: {code}")
    for _ in range(max_iterations):
        result = run_tests(code, tests)
        if result["success"]:
            return code
        code = llm(f"Fix error: {result['error']}\nCode: {code}")
    return code
```

## Evaluation Strategies

| Strategy | Use Case |
|----------|----------|
| **Outcome-Based** | Does output achieve expected result? |
| **LLM-as-Judge** | Compare and rank multiple outputs |
| **Rubric-Based** | Score against weighted dimensions (accuracy, clarity, completeness) |

## Best Practices

- Define specific, measurable evaluation criteria upfront
- Set max iterations (3-5) to prevent infinite loops
- Stop if score isn't improving between iterations
- Use structured JSON for reliable parsing of evaluations
- Log full trajectory for debugging
