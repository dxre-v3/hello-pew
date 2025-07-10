import { test, expect } from '@playwright/test';

test('App will display "Hello World!"', async({ page }) => {
    await page.goto('http://localhost:5173/hello-pew/');
    const helloWorldElement = await page.locator('#hello-world');
    const elementContent = await helloWorldElement.textContent();
    expect(elementContent).toBe('Hello World!');
})