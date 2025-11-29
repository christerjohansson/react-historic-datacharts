# Stock Market Analytics

A modern, interactive web application for visualizing historical stock price data. Built with Next.js, React, Tailwind CSS, and Recharts.

![Stock Market Analytics](https://placehold.co/800x400/1e293b/6366f1?text=Stock+Market+Analytics)

## Features

- **Interactive Visualizations**: Dynamic area charts showing Close and High prices over time.
- **Stock Selection**: Easy-to-use dropdown to switch between different stock symbols.
- **Data Insights**: Tooltips displaying precise price information on hover.
- **Responsive Design**: Fully responsive layout that works on desktop and mobile devices.
- **Dark Mode UI**: Sleek, modern dark theme using Tailwind CSS.

## Technology Stack

- **Framework**: [Next.js 15](https://nextjs.org/) (App Router)
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Charts**: [Recharts](https://recharts.org/)
- **Font**: [Geist](https://vercel.com/font)

## Getting Started

### Prerequisites

- Node.js (v18 or later recommended)
- npm, yarn, or pnpm

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd data-charts-react
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

### Running the Application

Run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Building for Production

To create an optimized production build:

```bash
npm run build
```

To start the production server:

```bash
npm start
```

## Project Structure

- `app/`: Contains the application source code (App Router).
  - `components/`: Reusable React components (`StockChart`, `StockSelector`).
  - `data/`: JSON data files containing stock prices.
  - `globals.css`: Global styles and Tailwind directives.
  - `layout.tsx`: Root layout component.
  - `page.tsx`: Main page component.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
