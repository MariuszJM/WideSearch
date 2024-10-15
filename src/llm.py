from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq


class LLMHandler:
    """Handler class to manage LLM initialization and invocation based on selected provider and model."""

    def __init__(self, llm_name="ollama", llm_model="llama3.2:latest"):
        """Initialize LLM models based on the selected provider and model."""
        self.llm = self.get_llm(llm_name, llm_model)
        self.llm_json = self.get_llm_json_mode(llm_name, llm_model)

    def get_llm(self, llm_name, llm_model):
        """Return the LLM instance based on the provider and model."""
        if llm_name == "ollama":
            llm = ChatOllama(model=llm_model, temperature=0)
            return llm
        elif llm_name == "groq":
            llm = ChatGroq(model=llm_model, temperature=0.0)
            return llm
        else:
            raise ValueError(f"Unknown LLM name: {llm_name}")

    def get_llm_json_mode(self, llm_name, llm_model):
        """Return the LLM instance configured for JSON output based on the provider and model."""
        if llm_name == "ollama":
            llm_json = ChatOllama(model=llm_model, temperature=0, format="json")
            return llm_json
        elif llm_name == "groq":
            llm_json = ChatGroq(
                model=llm_model, temperature=0.0
            ).with_structured_output(method="json_mode")
            return llm_json
        else:
            raise ValueError(f"Unknown LLM name: {llm_name}")

    def invoke_text(self, prompt):
        """Invoke the text-based LLM and return a response."""
        response = self.llm.invoke([prompt])
        return response.content.strip()

    def invoke_json(self, prompt):
        """Invoke the JSON-based LLM and return a response."""
        response = self.llm_json.invoke([prompt])
        return response.content
