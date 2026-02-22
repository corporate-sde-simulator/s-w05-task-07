import { TaxEngine } from "../src/taxEngine";
import { RegionConfig } from "../src/regionConfig";

describe("Tax calculation engine for multi-region", () => {
    test("should process valid input", () => {
        const obj = new TaxEngine();
        expect(obj.process({ key: "val" })).not.toBeNull();
    });
    test("should handle null", () => {
        const obj = new TaxEngine();
        expect(obj.process(null)).toBeNull();
    });
    test("should track stats", () => {
        const obj = new TaxEngine();
        obj.process({ x: 1 });
        expect(obj.getStats().processed).toBe(1);
    });
    test("support should work", () => {
        const obj = new RegionConfig();
        expect(obj.process({ data: "test" })).not.toBeNull();
    });
});
