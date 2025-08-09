"use client";

import axios from "axios";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import ShowMore from "@/components/showMore";
import MomentumChart from "@/components/chart";

type MarketPulseData = {
    ticker: string;
    as_of: string;
    momentum: {
        score: number;
        returns: Array<number>;
    };
    news: Array<{
        title: string;
        description: string;
        url: string;
    }>;
    pulse: string;
    llm_explanation: string;
}

export default function Home() {
    const [loading, setLoading] = useState<boolean>(false);
    const [ticker, setTicker] = useState<string>("");
    const [data, setData] = useState<null | MarketPulseData>(null);
    const [showFull, setShowFull] = useState<boolean>(false);
    const [chart, setChart] = useState<boolean>(false);

    const getPulseData = async () => {
        setLoading(true);
        // Implement search logic here
        console.log("Searching for:", ticker);
        try {
            const response = await axios.get(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/v1/market-pulse?ticker=${ticker}`);
            setData(response.data);
            console.log("Search results:", response.data);
        } catch (error) {
            console.error("API Error:", error);
            alert("Failed to fetch market pulse.");
        } finally {
            setLoading(false);
        }
    }

    const showFullData = () => {
        setShowFull(!showFull);
        setChart(false); // Hide chart when showing full data
        console.log("Toggling full data view:", !showFull);
        if (!showFull && data) {
            console.log("Full data:", data);
        }
        if (showFull) {
            console.log("Hiding full data");
        }
    }

    const showChart = () => {
        setChart(!chart);
        setShowFull(false); // Hide full data when showing chart
        console.log("Toggling chart view:", !chart);
        if (!chart && data) {
            console.log("Chart data:", data.momentum.returns);
        }
        if (chart) {
            console.log("Hiding chart");
        }
    }

    return (
        <div className="flex flex-col items-center justify-center">
            <main className="rounded-xl shadow-lg p-10 w-full max-w-4xl flex flex-col items-center">
                <h1 className="text-4xl font-extrabold text-blue-700 dark:text-blue-300 mb-4 text-center">
                    Welcome to Market-Pulse
                </h1>
                <p className="text-lg text-gray-700 dark:text-gray-300 mb-8 text-center">
                    Your one-stop solution for market insights and analytics.
                </p>
                <div className="w-full flex items-center gap-2">
                    <Input
                        placeholder="Search stocks, news, or analytics..."
                        className="flex-1 px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700 focus:ring-2 focus:ring-blue-400"
                        value={ticker}
                        onChange={(e) => setTicker(e.target.value)}
                    />
                    <Button className="px-6 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-semibold shadow" onClick={getPulseData}>
                        {loading ? "Searching..." : "Search"}
                    </Button>
                </div>
                {data && (
                    <div className="mt-8 w-full">
                        <h2 className="text-2xl font-bold text-blue-700 dark:text-blue-300 mb-4">Search Results</h2>
                        <p className="text-gray-700 dark:text-gray-300 mb-2">
                            <strong>LLM Explanation:</strong> {data.llm_explanation}
                        </p>
                        <div className="flex gap-4 mt-4">
                            <Button
                                variant={showFull ? "secondary" : "outline"}
                                className={`flex-1 transition-all duration-200 ${showFull ? "ring-2 ring-blue-400" : ""}`}
                                onClick={showFullData}
                            >
                                {showFull ? "Hide Full Data" : "Show Full Data"}
                            </Button>
                            <Button
                                variant={chart ? "secondary" : "outline"}
                                className={`flex-1 transition-all duration-200 ${chart ? "ring-2 ring-blue-400" : ""}`}
                                onClick={showChart}
                            >
                                {chart ? "Hide Chart" : "Show Chart"}
                            </Button>
                        </div>
                        {showFull && <ShowMore data={data} />}
                        {chart && <MomentumChart returns={data.momentum.returns} score={data.momentum.score} />}

                    </div>
                )}
            </main>
        </div>
    );
}
