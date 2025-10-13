async function addition(a: number, b: number): Promise<number> {
    console.log("Performing addition...");
    return a + b;
}

async function subtraction(a: number, b: number): Promise<number> {
    console.log("Performing subtraction...");
    return a - b;
}
async function multiplication(a: number, b: number): Promise<number> {
    console.log("Performing multiplication...");
    return a * b;
}

async function division(a: number, b: number): Promise<number> {
    console.log("Performing division...");
    if (b === 0) {
        throw new Error("Division by zero is not allowed.");
    }
    return a / b;
}

export { addition, subtraction, multiplication, division };

