// 使用语言为JavaScript
class AlertTemperature {
    constructor(freezingTemperature, boilingTemperature, fluctuation) {
      this.freezingTemperature = freezingTemperature; // 冻结阈值
      this.boilingTemperature = boilingTemperature; // 沸腾阈值
      this.fluctuation = fluctuation; // 波动范围
  
      this.freezing = "freezing";
      this.unfreezing = "unfreezing";
      this.boiling = "boiling";
      this.unboiling = "unboiling";
      this.currentFreezeType = ""; // freezing or unfreezing
      this.currentBoilType = ""; // boiling or unboiling
    }
  
    testTemperature(temperature) {
      // 沸腾
      if (temperature >= this.boilingTemperature) {
        return this.boilingFn(temperature);
      }
      // 冻结
      if (temperature <= this.freezingTemperature) {
        return this.freezeFn(temperature);
      }
      // 熟
      if (this.currentBoilType === this.boiling && temperature < this.boilingTemperature - this.fluctuation) {
        this.currentBoilType = this.unboiling;
        this.currentFreezeType = this.unfreezing;
        return this.alertFn(temperature, this.currentBoilType);
      }
      // 解冻
      if (this.currentFreezeType === this.freezing && temperature > this.freezingTemperature + this.fluctuation) {
        this.currentFreezeType = this.unfreezing;
        this.currentBoilType = this.unboiling;
        return this.alertFn(temperature, this.currentFreezeType);
      }
  
      return this.alertFn(temperature); 
    }
  
    freezeFn(temperature) {
      if (this.currentFreezeType === this.freezing) return this.alertFn(temperature);
      this.currentFreezeType = this.freezing;
      this.currentBoilType = this.unboiling;
      return this.alertFn(temperature, this.currentFreezeType);
    }
    boilingFn(temperature) {
      if (this.currentBoilType === this.boiling) return this.alertFn(temperature);
      this.currentBoilType = this.boiling;
      this.currentFreezeType = this.unfreezing;
      return this.alertFn(temperature, this.currentBoilType);
    }
    alertFn(temperature, type) {
      if (type) return `${temperature} ${type}`;
      return `${temperature}`;
    }
  }
  
  // test cases
  const alertTemperature = new AlertTemperature(0.0, 100, 0.5);
  const inputs = [4.0, 1.5, 1.0, 0.5, 0.0, -0.5, 100.5, 0.0, -1.0, -3.0, 1.0, 2.0, 5.0];
  for (const temp of inputs) {
    const res = alertTemperature.testTemperature(temp);
    console.log(res);
  }
  