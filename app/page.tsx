'use client'

import React, { useState } from 'react';
import StockSelector from './components/StockSelector';
import StockChart from './components/StockChart';
import priceHistoryData from './data/price-history.json';

interface YearData {
  close: number;
  high: number;
}

interface StockData {
  [year: string]: YearData;
}

interface PriceHistoryData {
  [symbol: string]: StockData;
}

export default function Home() {
  // Cast the imported JSON to the correct type
  const priceHistory: PriceHistoryData = priceHistoryData as unknown as PriceHistoryData;
  
  const stockSymbols = Object.keys(priceHistory).sort();
  const [selectedStock, setSelectedStock] = useState<string>(stockSymbols.length > 0 ? stockSymbols[0] : '');

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8 font-sans">
      <header className="mb-12 text-center">
        <h1 className="text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600 mb-4">
          Stock Market Analytics
        </h1>
        <p className="text-xl text-gray-400">
          Interactive Historical Stock Price Visualization
        </p>
      </header>

      <main className="max-w-6xl mx-auto space-y-8">
        <div className="bg-gray-800 rounded-2xl p-6 shadow-xl border border-gray-700">
          <StockSelector
            stocks={stockSymbols}
            selectedStock={selectedStock}
            onSelectStock={setSelectedStock}
          />
        </div>

        <div className="bg-gray-800 rounded-2xl p-8 shadow-xl border border-gray-700 min-h-[500px]">
          {selectedStock && priceHistory[selectedStock] ? (
            <StockChart
              stockSymbol={selectedStock}
              data={priceHistory[selectedStock]}
            />
          ) : (
            <div className="flex items-center justify-center h-full text-gray-500 text-xl">
              <p>Please select a stock to view its performance chart.</p>
            </div>
          )}
        </div>
      </main>

      <footer className="mt-16 text-center text-gray-500 text-sm">
        <p>Data spans from 2018 to 2022 | {stockSymbols.length} stocks available</p>
      </footer>
    </div>
  );
}