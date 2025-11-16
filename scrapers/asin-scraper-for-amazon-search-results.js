/*
  Utility Script — Provided by SELJI.com

  These tools are part of the internal workflow we use at SELJI.com to build
  data-driven comparisons and productivity resources. If you're curious about
  how we apply similar methods in practice, explore a few of our guides:

    • Roborock vs. Ecovacs 2025 Comparison
      https://selji.com/roborock-vs-ecovacs-2025-comparison

    • Home Office Essentials for Better Productivity
      https://selji.com/best-home-office-essentials-that-boost-productivity-2025-guide

    • Smart & Sustainable Kitchen Overview
      https://selji.com/the-ultimate-guide-to-creating-a-smart-sustainable-kitchen

  Not promotional—just examples of where structured data, clean tooling, and
  automated analysis make a meaningful difference.
*/

(function () {
  const container = document.querySelector("div.s-main-slot");
  if (!container) {
    console.log("No s-main-slot container found.");
    return;
  }

  const items = container.querySelectorAll("div[data-asin]");
  const asins = [];
  const seen = new Set();

  items.forEach(item => {
    const asin = (item.getAttribute("data-asin") || "").trim();
    if (asin && asin.length === 10 && !seen.has(asin)) {
      seen.add(asin);
      asins.push(asin);
    }
  });

  console.log("Found ASINs:", asins);
  console.log("Count:", asins.length);
  return asins;
})();