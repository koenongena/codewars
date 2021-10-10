/* Task: https://www.codewars.com/kata/5518a860a73e708c0a000027

 For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

 E. g.,

 last_digit([3, 4, 2]) == 1

 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

 Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

 Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.
 */

/**
 * Solution.
 *
 * The last digit of an expression x ^ y can be found by investigating whether y is divisible by 4.
 *
 * As such, finding the last digit of an expression x ^ (y ^ z), can be solved in 2 steps:
 *
 * 1. Find out whether y^z is divisible by 4. A number is divisible by 4 if the last 2 digits of a number are divisible by 4. In other words: we are only interest in the 2 last digits of y^z. Let's name these last 2 digits DD
 * 2. Find the last digit of x^DD. We already have that solution in last-digit-of-a-large-number.js
 *
 */

const tenth = (x) => Math.floor((x / 10)) % 10 * 10;
const unit = y => y % 10;

function handleUnitDigit1(x, y) {
    return ((tenth(x) * unit(y)) + 1) % 100;
}

function handleUnitDigit9(x, y) {
    if (y % 2 === 0) {
        return twoLastDigits(x ** 2, y / 2) % 100;
    } else {
        return twoLastDigits(x, (y - 1)) * x % 100;
    }
}

const twoLastDigits = (x, y) => {
    if (y === 0) {
        return 1;
    } else if (y === 1) {
        return x;
    }

    switch (x % 10) {
        case 1:
            return handleUnitDigit1(x, y);
        case 9:
            return handleUnitDigit9(x, y);
        default:
            return undefined;
    }
};

module.exports = {
    twoLastDigits
}