/* =========================================================
   CLEARSETTLE — FRONTEND JAVASCRIPT
========================================================= */


/* =========================================================
   1. DEMO TRANSACTION DATA
   Temporary frontend data.
   Later this will come from the backend API.
========================================================= */

const transactions = {

    "TXN-88213-GT": {
        id: "TXN-88213-GT",
        amount: "₹24,500",
        date: "04 Sep 2026, 10:42 AM",
        status: "Delayed",
        confidence: 94,

        explanation:
            "The transaction was successfully received by the Gateway and processed by the Bank, but the Ledger has not yet recorded the final settlement. This indicates a settlement synchronization delay rather than an initial payment failure.",

        exception:
            "Settlement delay detected between Bank confirmation and Ledger posting.",

        diagnosis:
            "The payment completed successfully through the Gateway and Bank, but the final Ledger update is delayed.",

        factors: [
            "Gateway accepted the transaction successfully.",
            "Bank processing completed successfully.",
            "Ledger confirmation is still pending.",
            "The delay appears to be occurring during settlement synchronization."
        ],

        recommendation:
            "Monitor the Ledger posting and retry the settlement synchronization if the transaction remains pending.",

        timeline: [
            {
                time: "10:42 AM",
                title: "Transaction Initiated",
                description:
                    "Customer initiated the payment transaction.",
                status: "completed"
            },
            {
                time: "10:42 AM",
                title: "Gateway Processed",
                description:
                    "Payment Gateway accepted and processed the transaction.",
                status: "completed"
            },
            {
                time: "10:43 AM",
                title: "Bank Confirmed",
                description:
                    "Bank successfully processed the payment.",
                status: "completed"
            },
            {
                time: "10:45 AM",
                title: "Ledger Update",
                description:
                    "Ledger posting is still pending.",
                status: "pending"
            }
        ],

        systems: {
            gateway: {
                title: "Gateway",
                status: "Success",
                transactionId: "GT-88213",
                response: "Payment Accepted",
                timestamp: "10:42:13 AM"
            },

            bank: {
                title: "Bank",
                status: "Success",
                transactionId: "BNK-88213",
                response: "Settlement Confirmed",
                timestamp: "10:43:07 AM"
            },

            ledger: {
                title: "Ledger",
                status: "Pending",
                transactionId: "LED-88213",
                response: "Posting Pending",
                timestamp: "10:45:31 AM"
            }
        }
    },


    "TXN-44192-BK": {
        id: "TXN-44192-BK",
        amount: "₹8,750",
        date: "03 Sep 2026, 03:18 PM",
        status: "Failed",
        confidence: 97,

        explanation:
            "The transaction reached the Gateway, but the Bank rejected the payment during authorization. Because the Bank did not confirm the transaction, the Ledger correctly did not record a successful settlement.",

        exception:
            "Bank authorization failure detected.",

        diagnosis:
            "The transaction failed at the Bank authorization stage.",

        factors: [
            "Gateway successfully received the payment request.",
            "Bank rejected the authorization request.",
            "No successful Bank settlement confirmation was received.",
            "Ledger did not post the transaction."
        ],

        recommendation:
            "Verify the Bank rejection reason and retry the transaction after resolving the authorization issue.",

        timeline: [
            {
                time: "03:18 PM",
                title: "Transaction Initiated",
                description:
                    "Customer initiated the payment.",
                status: "completed"
            },
            {
                time: "03:18 PM",
                title: "Gateway Processed",
                description:
                    "Gateway accepted the transaction request.",
                status: "completed"
            },
            {
                time: "03:18 PM",
                title: "Bank Authorization",
                description:
                    "Bank rejected the authorization request.",
                status: "exception"
            },
            {
                time: "03:19 PM",
                title: "Ledger",
                description:
                    "No settlement posting was created.",
                status: "exception"
            }
        ],

        systems: {
            gateway: {
                title: "Gateway",
                status: "Success",
                transactionId: "GT-44192",
                response: "Payment Accepted",
                timestamp: "03:18:04 PM"
            },

            bank: {
                title: "Bank",
                status: "Failed",
                transactionId: "BNK-44192",
                response: "Authorization Declined",
                timestamp: "03:18:22 PM"
            },

            ledger: {
                title: "Ledger",
                status: "Failed",
                transactionId: "LED-44192",
                response: "No Posting",
                timestamp: "03:19:01 PM"
            }
        }
    },


    "TXN-10983-LD": {
        id: "TXN-10983-LD",
        amount: "₹15,200",
        date: "02 Sep 2026, 11:06 AM",
        status: "Success",
        confidence: 99,

        explanation:
            "The transaction completed successfully across all three systems. The Gateway accepted the payment, the Bank confirmed settlement, and the Ledger recorded the final transaction.",

        exception:
            "No exception detected. All three systems are consistent.",

        diagnosis:
            "No settlement issue detected. The transaction was successfully completed.",

        factors: [
            "Gateway accepted the transaction.",
            "Bank confirmed successful settlement.",
            "Ledger recorded the settlement.",
            "Transaction states are consistent across all systems."
        ],

        recommendation:
            "No action required. The transaction has settled successfully.",

        timeline: [
            {
                time: "11:06 AM",
                title: "Transaction Initiated",
                description:
                    "Customer initiated the payment.",
                status: "completed"
            },
            {
                time: "11:06 AM",
                title: "Gateway Processed",
                description:
                    "Gateway accepted the transaction.",
                status: "completed"
            },
            {
                time: "11:07 AM",
                title: "Bank Confirmed",
                description:
                    "Bank confirmed successful settlement.",
                status: "completed"
            },
            {
                time: "11:08 AM",
                title: "Ledger Posted",
                description:
                    "Ledger successfully recorded the settlement.",
                status: "completed"
            }
        ],

        systems: {
            gateway: {
                title: "Gateway",
                status: "Success",
                transactionId: "GT-10983",
                response: "Payment Accepted",
                timestamp: "11:06:12 AM"
            },

            bank: {
                title: "Bank",
                status: "Success",
                transactionId: "BNK-10983",
                response: "Settlement Confirmed",
                timestamp: "11:07:04 AM"
            },

            ledger: {
                title: "Ledger",
                status: "Success",
                transactionId: "LED-10983",
                response: "Posting Complete",
                timestamp: "11:08:15 AM"
            }
        }
    }

};


/* =========================================================
   2. DOM ELEMENTS
========================================================= */

const searchInput =
    document.getElementById("transactionSearch");

const searchButton =
    document.getElementById("searchButton");

const transactionStatus =
    document.getElementById("transactionStatus");

const displayTransactionId =
    document.getElementById("displayTransactionId");

const displayAmount =
    document.getElementById("displayAmount");

const displayDate =
    document.getElementById("displayDate");

const displaySettlementStatus =
    document.getElementById("displaySettlementStatus");

const aiExplanation =
    document.getElementById("aiExplanation");

const confidenceValue =
    document.getElementById("confidenceValue");

const confidenceBar =
    document.getElementById("confidenceBar");

const exceptionMessage =
    document.getElementById("exceptionMessage");

const timeline =
    document.getElementById("timeline");

const systemTrace =
    document.getElementById("systemTrace");

const diagnosisResult =
    document.getElementById("diagnosisResult");

const recommendation =
    document.getElementById("recommendation");

const qaInput =
    document.getElementById("qaInput");

const qaSendButton =
    document.getElementById("qaSendButton");

const qaMessages =
    document.getElementById("qaMessages");


/* =========================================================
   3. CURRENT TRANSACTION
========================================================= */

let currentTransaction = null;

let currentSystem = "gateway";


/* =========================================================
   4. SEARCH TRANSACTION
========================================================= */

function searchTransaction() {

    async function searchTransaction() {

    const query = searchInput.value.trim().toUpperCase();

    if (!query) {
        alert("Please enter a transaction ID.");
        return;
    }

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/investigate/${query}`
        );

        if (!response.ok) {
            throw new Error("Transaction not found");
        }

        const data = await response.json();

        console.log("BACKEND DATA:", data);

        currentTransaction = data;

        updateTransactionInfo(data);
        updateExplanation(data);
        updateTimeline(data);
        updateSystemTrace(data, currentSystem);
        updateDiagnosis(data);
        updateRecommendation(data);

        clearQA();

    } catch (error) {

        console.error("Backend error:", error);

        alert("Could not find transaction or connect to backend.");
    }
}

/* =========================================================
   5. TRANSACTION INFORMATION
========================================================= */

function updateTransactionInfo(transaction) {

    displayTransactionId.textContent =
        transaction.id;

    displayAmount.textContent =
        transaction.amount;

    displayDate.textContent =
        transaction.date;

    displaySettlementStatus.textContent =
        transaction.status;

    transactionStatus.textContent =
        transaction.status;


    transactionStatus.className =
        "status-badge";


    if (transaction.status === "Success") {

        transactionStatus.style.background =
            "rgba(163, 191, 163, 0.28)";

        transactionStatus.style.color =
            "#6E8F6E";

    } else if (transaction.status === "Failed") {

        transactionStatus.style.background =
            "#F6D3D5";

        transactionStatus.style.color =
            "#B15A61";

    } else {

        transactionStatus.style.background =
            "rgba(230, 213, 176, 0.45)";

        transactionStatus.style.color =
            "#A8863F";
    }
}


/* =========================================================
   6. AI EXPLANATION
========================================================= */

function updateExplanation(transaction) {

    aiExplanation.textContent =
        transaction.explanation;


    confidenceValue.textContent =
        `${transaction.confidence}%`;


    confidenceBar.style.width =
        `${transaction.confidence}%`;


    exceptionMessage.textContent =
        transaction.exception;
}


/* =========================================================
   7. TIMELINE
========================================================= */

function updateTimeline(transaction) {

    timeline.innerHTML = "";


    transaction.timeline.forEach((event) => {

        const item =
            document.createElement("div");

        item.className =
            "timeline-item";


        const node =
            document.createElement("div");

        node.className =
            `timeline-node ${event.status}`;


        const content =
            document.createElement("div");


        const top =
            document.createElement("div");

        top.className =
            "timeline-top";


        const time =
            document.createElement("span");

        time.className =
            "timeline-time";

        time.textContent =
            event.time;


        const status =
            document.createElement("span");

        status.className =
            `status-pill ${event.status}`;

        status.textContent =
            getStatusLabel(event.status);


        top.appendChild(time);

        top.appendChild(status);


        const title =
            document.createElement("div");

        title.className =
            "timeline-title";

        title.textContent =
            event.title;


        const description =
            document.createElement("div");

        description.className =
            "timeline-description";

        description.textContent =
            event.description;


        content.appendChild(top);

        content.appendChild(title);

        content.appendChild(description);


        item.appendChild(node);

        item.appendChild(content);


        timeline.appendChild(item);

    });

}


/* =========================================================
   8. TIMELINE STATUS LABEL
========================================================= */

function getStatusLabel(status) {

    if (status === "completed") {
        return "Completed";
    }

    if (status === "pending") {
        return "Pending";
    }

    if (status === "exception") {
        return "Exception";
    }

    return status;
}


/* =========================================================
   9. SYSTEM TRACE
========================================================= */

function updateSystemTrace(
    transaction,
    system
) {

    const data =
        transaction.systems[system];


    if (!data) {
        return;
    }


    const statusClass =
        data.status === "Success"
            ? "success"
            : "failed";


    systemTrace.innerHTML = `

        <div class="trace-box">

            <div class="trace-box-top">

                <div class="trace-number ${statusClass}">
                    ${getSystemNumber(system)}
                </div>

                <div class="trace-title">
                    ${data.title}
                </div>

                <span
                    class="status-pill ${
                        data.status === "Success"
                            ? "success"
                            : "failed"
                    }"
                    style="margin-left:auto;"
                >
                    ${data.status}
                </span>

            </div>


            <div class="trace-line">

                <span class="label">
                    Transaction ID
                </span>

                <span class="value">
                    ${data.transactionId}
                </span>

            </div>


            <div class="trace-line">

                <span class="label">
                    Response
                </span>

                <span class="value">
                    ${data.response}
                </span>

            </div>


            <div class="trace-line">

                <span class="label">
                    Timestamp
                </span>

                <span class="value">
                    ${data.timestamp}
                </span>

            </div>

        </div>
    `;
}


/* =========================================================
   10. SYSTEM NUMBER
========================================================= */

function getSystemNumber(system) {

    if (system === "gateway") {
        return "1";
    }

    if (system === "bank") {
        return "2";
    }

    return "3";
}


/* =========================================================
   11. DIAGNOSIS
========================================================= */

function updateDiagnosis(transaction) {

    const factorsHTML =
        transaction.factors
            .map(
                factor => `<li>${factor}</li>`
            )
            .join("");


    diagnosisResult.innerHTML = `

        <p class="diagnosis-text">
            ${transaction.diagnosis}
        </p>

        <ul class="diagnosis-factors">
            ${factorsHTML}
        </ul>

    `;
}


/* =========================================================
   12. RECOMMENDATION
========================================================= */

function updateRecommendation(transaction) {

    recommendation.textContent =
        transaction.recommendation;
}


/* =========================================================
   13. SYSTEM TABS
========================================================= */

const systemTabs =
    document.querySelectorAll(".system-tab");


systemTabs.forEach((tab) => {

    tab.addEventListener("click", () => {

        systemTabs.forEach((item) => {
            item.classList.remove("active");
        });


        tab.classList.add("active");


        currentSystem =
            tab.dataset.system;


        if (currentTransaction) {

            updateSystemTrace(
                currentTransaction,
                currentSystem
            );

        }

    });

});


/* =========================================================
   14. FILTER BUTTONS
========================================================= */

const filterButtons =
    document.querySelectorAll(".filter-button");


filterButtons.forEach((button) => {

    button.addEventListener("click", () => {

        filterButtons.forEach((item) => {
            item.classList.remove("active");
        });


        button.classList.add("active");


        const filter =
            button.dataset.filter;


        handleFilter(filter);

    });

});


function handleFilter(filter) {

    if (filter === "all") {
        return;
    }


    const matchingTransactions =
        Object.values(transactions)
            .filter((transaction) => {

                if (filter === "success") {
                    return transaction.status === "Success";
                }

                if (filter === "failed") {
                    return transaction.status === "Failed";
                }

                if (filter === "pending") {
                    return transaction.status === "Delayed";
                }

                return true;
            });


    if (matchingTransactions.length > 0) {

        const first =
            matchingTransactions[0];

        searchInput.value =
            first.id;

        searchTransaction();

    }

}


/* =========================================================
   15. SEARCH BUTTON
========================================================= */

searchButton.addEventListener(
    "click",
    searchTransaction
);


/* =========================================================
   16. ENTER KEY SEARCH
========================================================= */

searchInput.addEventListener(
    "keydown",
    (event) => {

        if (event.key === "Enter") {

            searchTransaction();

        }

    }
);


/* =========================================================
   17. Q&A
========================================================= */

function addQAMessage(
    type,
    message
) {

    const wrapper =
        document.createElement("div");

    wrapper.className =
        `qa-message ${type}`;


    const content =
        document.createElement("div");

    content.className =
        "message-content";


    const label =
        document.createElement("div");

    label.className =
        "message-label";

    label.textContent =
        type === "user"
            ? "You"
            : "ClearSettle AI";


    const text =
        document.createElement("div");

    text.className =
        "message-text";

    text.textContent =
        message;


    content.appendChild(label);

    content.appendChild(text);


    wrapper.appendChild(content);


    qaMessages.appendChild(wrapper);


    qaMessages.scrollTop =
        qaMessages.scrollHeight;
}


/* =========================================================
   18. CLEAR Q&A
========================================================= */

function clearQA() {

    qaMessages.innerHTML = "";


    addQAMessage(
        "assistant",
        "Transaction loaded. Ask me anything about its settlement journey."
    );

}


/* =========================================================
   19. Q&A RESPONSE
========================================================= */

function answerQuestion(question) {

    if (!currentTransaction) {

        return "Please search for a transaction first.";

    }


    const q =
        question.toLowerCase();


    if (
        q.includes("why") &&
        (
            q.includes("fail") ||
            q.includes("delay")
        )
    ) {

        return currentTransaction.diagnosis;
    }


    if (
        q.includes("status")
    ) {

        return `The current settlement status is ${currentTransaction.status}.`;
    }


    if (
        q.includes("gateway")
    ) {

        const data =
            currentTransaction.systems.gateway;

        return `Gateway status: ${data.status}. ${data.response}.`;
    }


    if (
        q.includes("bank")
    ) {

        const data =
            currentTransaction.systems.bank;

        return `Bank status: ${data.status}. ${data.response}.`;
    }


    if (
        q.includes("ledger")
    ) {

        const data =
            currentTransaction.systems.ledger;

        return `Ledger status: ${data.status}. ${data.response}.`;
    }


    if (
        q.includes("amount") ||
        q.includes("money")
    ) {

        return `The transaction amount is ${currentTransaction.amount}.`;
    }


    if (
        q.includes("recommend") ||
        q.includes("action") ||
        q.includes("next")
    ) {

        return currentTransaction.recommendation;
    }


    return currentTransaction.explanation;
}


/* =========================================================
   20. SEND Q&A
========================================================= */

function sendQuestion() {

    const question =
        qaInput.value.trim();


    if (!question) {
        return;
    }


    addQAMessage(
        "user",
        question
    );


    const answer =
        answerQuestion(question);


    setTimeout(() => {

        addQAMessage(
            "assistant",
            answer
        );

    }, 250);


    qaInput.value = "";

}


/* =========================================================
   21. Q&A BUTTON
========================================================= */

qaSendButton.addEventListener(
    "click",
    sendQuestion
);


/* =========================================================
   22. Q&A ENTER KEY
========================================================= */

qaInput.addEventListener(
    "keydown",
    (event) => {

        if (event.key === "Enter") {

            sendQuestion();

        }

    }
);
