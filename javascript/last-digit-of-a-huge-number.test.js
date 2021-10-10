const {twoLastDigits} = require("./last-digit-of-a-huge-number");
describe("Last 2 digits", () => {
    it('should return 1 number of the exponent is too small', function () {
        expect(twoLastDigits('1', '2')).toEqual(1)
    });

    it('should calculate last 2 digits of unit digit 1', function () {
        expect(twoLastDigits("91", "246")).toEqual(41);
    });

})