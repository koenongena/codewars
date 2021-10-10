const {twoLastDigits} = require("./last-digit-of-a-huge-number");

describe("Last 2 digits", () => {
    it('should return 1 number of the exponent is too small', function () {
        expect(twoLastDigits(1, 2)).toEqual(1)
    });

    it('should calculate last 2 digits of unit digit 1', function () {
        expect(twoLastDigits(91, 246)).toEqual(41);
    });

    it('should calculate last digits of unit digit 9 and even exponent', () => {
        expect(twoLastDigits("9", "2")).toEqual(81);
        expect(twoLastDigits("79", "142")).toEqual(41);
    });

    it('should calculate last digits of unit digit 9 and with odd exponent', function () {
        expect(twoLastDigits("79", "143")).toEqual(39);
    });

    it('should handle large numbers for unit digit 9', function () {
        expect(twoLastDigits(694029, 140249)).toEqual(69)
    });

    it('should calculate unit digit 3 and small exponents', function () {
        expect(twoLastDigits(3, 1)).toEqual(3);
        expect(twoLastDigits(3, 2)).toEqual(9)
        expect(twoLastDigits(3, 3)).toEqual(27)
        expect(twoLastDigits(3, 4)).toEqual((27 * 3) % 100)
    });

    it('should handle even exponents unit digit 3', function () {
        expect(twoLastDigits(79, 142)).toEqual(41);
    });

    it('should handle odd exponents unit digit 3', function () {
        expect(twoLastDigits(79, 143)).toEqual((41 * 79) % 100);
    });

    it('should handle unit digit 7', function () {
        expect(twoLastDigits(7, 2)).toEqual(Math.pow(7, 2))
        expect(twoLastDigits(7, 3)).toEqual(Math.pow(7, 3) % 100);
        expect(twoLastDigits(7, 4)).toEqual(Math.pow(7, 4) % 100);
    });

    it('should handle unit digit 7 for larger even exponents', function () {
        expect(twoLastDigits(17, 256)).toEqual(81);
    });
    it('should handle unit digit 7 for larger odd exponents', function () {
        expect(twoLastDigits(17, 257)).toEqual((81 * 17) % 100);
    });

    it('should handle unit digit 2 for small exponent', function () {
        expect(twoLastDigits(2, 1)).toEqual(2);
        expect(twoLastDigits(2, 2)).toEqual(4);

    });
    it('should handle unit digit 2 large numbers', function () {
        expect(twoLastDigits(98729348732, 2)).toEqual(20);
    });

    it('should handle unit digit 2 large exponents', function () {
        expect(twoLastDigits(2, 1056)).toEqual(36);
    });

    it('should handle unit digit 8 large exponents', function () {
        //two last numbers of 2^3^1056 = (2^1056) * (2^1056) * (2^1056)
        expect(twoLastDigits(8, 1056)).toEqual((36 * 36 * 36) % 100);
    });

    it('should handle unit digit 5', function () {
        expect(twoLastDigits(65, 243)).toEqual(25);
        expect(twoLastDigits(135, 1091)).toEqual(75);
    });

    it('should handle unit digit 0', function () {
        expect(twoLastDigits(0, 0)).toEqual(1);
        expect(twoLastDigits(0, 1056)).toEqual(0);
        expect(twoLastDigits(10, 1056)).toEqual(0);
        expect(twoLastDigits(100, 1056)).toEqual(0);
    });
});