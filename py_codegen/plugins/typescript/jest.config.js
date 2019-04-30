module.exports = {
  "roots": [
    // "<rootDir>/src",
    "<rootDir>/__tests__",
  ],
  "bail": true,
  "testEnvironment": "node",
  "testMatch": [
    "**/?(*.)+(spec|test).ts?(x)",
    "**/test.ts?(x)"
  ],
  "testPathIgnorePatterns": [
    "/node_modules/",
    "/ts_compiled/",
  ],
  "transform": {
    "^.+\\.tsx?$": "ts-jest",
  },
  "moduleFileExtensions": [
    "js",
    "json",
    "jsx",
    "node",
    "ts",
    "tsx",
  ],
  // "setupTestFrameworkScriptFile": "<rootDir>/jestSetupTestFramework.js"
}