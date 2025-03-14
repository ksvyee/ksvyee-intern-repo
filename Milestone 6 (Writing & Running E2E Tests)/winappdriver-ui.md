# Writing & Running E2E Tests

## Interacting with Native Windows UI Elements

### Reflections

**How do you locate and interact with Windows UI elements in WinAppDriver?**

I use element locators like Class Name and Name. I first inspect the UI using Inspect.exe to find the correct attributes and then use Appium’s find_element() methods to interact with them.

**What are the different ways to find elements (e.g., XPath, Accessibility ID)?**

XPath is flexible but slower. Accessibility ID is the fastest and most reliable if available. Class Name works well for common controls like buttons and text fields. Name is useful when elements have clear labels.

**How would you handle UI elements that load dynamically?**

I use implicit or explicit waits to give the elements time to appear. Explicit waits with conditions to help when elements take longer to load. If necessary, I check for element states before interacting with them.

**What are common challenges when automating native Windows UI interactions?**

Common challenges in automating native Windows UI include finding stable locators, handling popups, and dealing with inconsistent UI structures. Sometimes, elements don't have proper IDs, making XPath the only option. Synchronization issues can also cause tests to fail if elements aren’t ready in time.
