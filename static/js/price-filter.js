document.addEventListener("DOMContentLoaded", function() {

  const range = document.getElementById("priceRange");
  const rangeValue = document.getElementById("rangeValue");
  const minInput = document.getElementById("minPrice");
  const maxInput = document.getElementById("maxPrice");


  if (range) {

      // Update text when slider changes
      range.addEventListener("input", function() {
        if (rangeValue) rangeValue.innerText = "Current: " + this.value;
        if (minInput) minInput.value = 0;
        if (maxInput) maxInput.value = this.value;
      });

      // Update slider when max input changes
      if (maxInput) {
          maxInput.addEventListener("input", function() {
            range.value = this.value;
            if (rangeValue) rangeValue.innerText = "Current: " + this.value;
          });
      }
  }
});