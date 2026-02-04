---
name: react
description: Create a new React project with TypeScript, testing, and common configurations.
---

# React Scaffold Skill

Initialize React projects with best-practice configurations.

## Steps

1. **Create Project** (choose one method):
   ```bash
   # Using Vite (recommended)
   npm create vite@latest {project-name} -- --template react-ts

   # Using Create React App (legacy)
   npx create-react-app {project-name} --template typescript
   ```

2. **Add Common Dependencies** (if requested):
   ```bash
   cd {project-name}

   # Tailwind CSS
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p

   # Testing
   npm install -D vitest @testing-library/react @testing-library/jest-dom

   # Routing
   npm install react-router-dom

   # State Management
   npm install zustand  # or @reduxjs/toolkit react-redux
   ```

3. **Configure Files**:
   - `tailwind.config.js` - Configure content paths
   - `vite.config.ts` - Add test configuration
   - `tsconfig.json` - Verify strict mode

4. **Output**:
   ```
   ## React Project Created: {project-name}

   ### Structure
   {project-name}/
   ├── src/
   │   ├── App.tsx
   │   ├── main.tsx
   │   └── index.css
   ├── package.json
   ├── tsconfig.json
   ├── vite.config.ts
   └── tailwind.config.js

   ### Commands
   - `npm run dev` - Start dev server
   - `npm run build` - Production build
   - `npm run test` - Run tests
   ```

## Example Usage
- `/scaffold:react my-app`
- `/scaffold:react my-app --typescript --tailwind`
- `/scaffold:react dashboard --router --zustand`
