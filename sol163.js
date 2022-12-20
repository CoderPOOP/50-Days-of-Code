// Link - https://exercism.org/tracks/javascript/exercises/freelancer-rates/edit

// @ts-check
/**
 * The day rate, given a rate per hour
 *
 * @param {number} ratePerHour
 * @returns {number} the rate per day
 */
 export function dayRate(ratePerHour) {
    return 8 * ratePerHour;
  }
  /**
   * Calculates the number of days in a budget, rounded down
   *
   * @param {number} budget the total budget
   * @param {number} ratePerHour the rate per hour
   * @returns {number} the number of days
   */
  export function daysInBudget(budget, ratePerHour) {
    return Math.floor(budget / dayRate(ratePerHour))
  }
  /**
   * Calculates the rate per month
   *
   * @param {number} ratePerHour
   * @param {number} days
   * @param {number} discount for example 20% written as 0.2
   * @returns {number} the rounded up monthly rate
   */
  export function priceWithMonthlyDiscount(ratePerHour, days, discount) {
    const months = Math.floor(days / 22)
    const remainder = days % 22
    
    return Math.ceil(
      applyDiscount(22 * dayRate(ratePerHour) * months, discount) + 
      remainder * dayRate(ratePerHour)
    );
  }
  /**
   * Applies a discount to the value
   *
   * @param {number} value
   * @param {number} percentage for example 20% written as 0.2
   * @returns {number} the discounted value
   */
  function applyDiscount(value, percentage) {
    return Math.ceil(value * (1 - percentage))
  }
  