import React from 'react'

type Props = {
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

function renderValue(
    key: string,
    value: Props[keyof Props]
) {
    if (key === "momentum" && typeof value === "object" && value !== null && "score" in value && "returns" in value) {
        const momentumValue = value as Props["momentum"];
        return (
            <div className="space-y-1">
                <div>
                    <span className="font-medium">Score:</span> {momentumValue.score}
                </div>
                <div>
                    <span className="font-medium">Returns:</span>{" "}
                    <span className="text-xs">{JSON.stringify(momentumValue.returns)}</span>
                </div>
            </div>
        )
    }
    if (key === "news" && Array.isArray(value)) {
        return (
            <ul className="space-y-2">
                {(value as Props["news"]).map((item, idx) => (
                    <li key={idx} className="border-b pb-2 last:border-b-0">
                        <a href={item.url} target="_blank" rel="noopener noreferrer" className="font-semibold text-blue-600 hover:underline">
                            {item.title}
                        </a>
                        <div className="text-sm text-gray-600 dark:text-gray-400">{item.description}</div>
                    </li>
                ))}
            </ul>
        )
    }
    if (typeof value === "object" && value !== null) {
        return <pre className="bg-gray-100 dark:bg-gray-800 rounded p-2 text-xs">{JSON.stringify(value, null, 2)}</pre>
    }
    return <span>{String(value)}</span>
}

type ShowMoreProps = {
    data: Props;
};

export default function ShowMore({ data }: ShowMoreProps) {
    return (
        <div className="bg-white dark:bg-gray-900 rounded-lg shadow p-6">
            <h3 className="text-xl font-bold text-gray-800 dark:text-gray-200 mb-4">Additional Information</h3>
            <table className="w-full text-left border-separate border-spacing-y-2">
                <tbody>
                    {Object.entries(data).map(([key, value]) => (
                        <tr key={key} className="align-top">
                            <th className="pr-4 text-gray-700 dark:text-gray-300 font-semibold capitalize whitespace-nowrap">{key.replace(/_/g, " ")}</th>
                            <td className="text-gray-800 dark:text-gray-200">{renderValue(key, value)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}