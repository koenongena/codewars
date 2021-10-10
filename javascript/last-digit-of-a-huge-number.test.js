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

    it('should handle large numbers', function () {
        expect(twoLastDigits(694029, 140249)).toEqual(69)
    });
});