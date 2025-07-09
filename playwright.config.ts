import { PlaywrightTestConfig } from "@playwright/test";

const config: PlaywrightTestConfig = {
    webServer: {
        command: 'npm run dev',
        url: 'http://localhost:5173/hello/'
    },
};

export default config;