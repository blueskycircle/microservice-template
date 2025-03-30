from fastapi import FastAPI
from pydantic import BaseModel
from library.methods import add, subtract

app = FastAPI(
    title="Math Operations API",
    description="API for performing basic math operations",
    version="1.0.0",
)


class CalculationRequest(BaseModel):
    a: float
    b: float


class CalculationResponse(BaseModel):
    operation: str
    a: float
    b: float
    result: float


@app.get("/")
def read_root():
    """Root endpoint returning welcome message."""
    return {"message": "Welcome to the Math Operations API"}


@app.post("/add", response_model=CalculationResponse)
def addition(request: CalculationRequest):
    """Add two numbers and return the result."""
    result = add(request.a, request.b)
    return {"operation": "addition", "a": request.a, "b": request.b, "result": result}


@app.post("/subtract", response_model=CalculationResponse)
def subtraction(request: CalculationRequest):
    """Subtract two numbers and return the result."""
    result = subtract(request.a, request.b)
    return {
        "operation": "subtraction",
        "a": request.a,
        "b": request.b,
        "result": result,
    }


@app.get("/add/{a}/{b}", response_model=CalculationResponse)
def addition_get(a: float, b: float):
    """Add two numbers using GET request."""
    result = add(a, b)
    return {"operation": "addition", "a": a, "b": b, "result": result}


@app.get("/subtract/{a}/{b}", response_model=CalculationResponse)
def subtraction_get(a: float, b: float):
    """Subtract two numbers using GET request."""
    result = subtract(a, b)
    return {"operation": "subtraction", "a": a, "b": b, "result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
