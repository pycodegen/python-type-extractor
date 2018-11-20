module.exports = {
  "roots": [
    "<rootDir>/src",
    "<rootDir>/tests",
  ],
  "bail": true,
  "testEnvironment": "node",
  "testMatch": [
    "**/?(*.)+(spec|test).ts?(x)"
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