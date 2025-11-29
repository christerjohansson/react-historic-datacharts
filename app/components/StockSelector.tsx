'use client'

import React from 'react';

interface StockSelectorProps {
    stocks: string[];
    selectedStock: string;
    onSelectStock: (stock: string) => void;
}

export default function StockSelector({ stocks, selectedStock, onSelectStock }: StockSelectorProps) {
    return (
        <div className="flex flex-col sm:flex-row items-center gap-4">
            <label htmlFor="stock-select" className="text-gray-300 font-medium text-lg">
                Select Stock Symbol:
            </label>
            <div className="relative w-full sm:w-64">
                <select
                    id="stock-select"
                    value={selectedStock}
                    onChange={(e) => onSelectStock(e.target.value)}
                    className="w-full appearance-none bg-gray-900 border border-gray-600 text-white py-3 px-4 pr-8 rounded-lg leading-tight focus:outline-none focus:bg-gray-800 focus:border-blue-500 transition-colors cursor-pointer"
                >
                    <option value="" disabled>-- Choose a stock --</option>
                    {stocks.map((stock) => (
                        <option key={stock} value={stock}>
                            {stock}
                        </option>
                    ))}
                </select>
                <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-400">
                    <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                    </svg>
                </div>
            </div>
        </div>
    );
}
