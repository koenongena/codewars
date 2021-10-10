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

const tenth = (x) => Math.floor((x / 10)) % 10;
const unit = y => y % 10;

function handleUnitDigit1(x, y) {
    return ((tenth(x) * 10 * unit(y)) + 1) % 100;
}

const handleBaseRaise = (raise) => (x, y) => {
    if (y < raise) {
        return (x ** y) % 100;
    } else {
        return (twoLastDigits(x ** raise, Math.floor(y / raise)) * twoLastDigits(x, y % raise)) % 100;
    }
}
const handleUnitDigit9 = handleBaseRaise(2);
const handleUnitDigit3 = handleBaseRaise(4);
const handleUnitDigit7 = handleBaseRaise(4);

const handleUnitDigit2 = (x, y) => {
    if (y < 10) {
        return Math.pow(x, y) % 100;
    }

    return twoLastDigits(24, Math.floor(y / 10)) * twoLastDigits(2, y % 10) % 100;
};

const isOdd = x => x % 2 === 1;
const isEven = x => x % 2 === 0;

const handleUnitDigit5 = (x, y) => {
    if (isOdd(tenth(x)) && isOdd(y)) {
        return 75;
    } else {
        return 25;
    }
};

const twoLastDigits = (x, y) => {
    if (y === 0) {
        return 1;
    } else if (y === 1) {
        return x;
    } else if (x === 24 && isOdd(y)) {
        return 24;
    } else if (x === 24 && isEven(y)) {
        return 76;
    } else if (x === 76) {
        return 76;
    }

    switch (x % 10) {
        case 0:
            return 0;
        case 1:
            return handleUnitDigit1(x, y);
        case 9:
            return handleUnitDigit9(x, y);
        case 3:
            return handleUnitDigit3(x, y);
        case 7:
            return handleUnitDigit7(x, y);
        case 2:
        case 4:
        case 6:
        case 8:
            return handleUnitDigit2(2, y) * twoLastDigits(x / 2, y) % 100;
        case 5:
            return handleUnitDigit5(x, y);
        default:
            return undefined;
    }
};

module.exports = {
    twoLastDigits
}