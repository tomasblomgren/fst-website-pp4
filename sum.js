function sum(a, b) {
    return a + b;
}
module.exports = sum;

const addition = require("../sum.js");

describe("Calculator", () => {
    describe("Addition function", () => {
        test("should return 42 for 20 + 22", () => {
            expect(addition(20, 22).toBe(42));
        })
    });
    describe("Subtraction function", () => {

    });
    describe("Multiply function", () => {

    });
    describe("Division function", () => {

    });
})