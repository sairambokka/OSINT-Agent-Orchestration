# OSINT Agent Orchestration

A powerful multi-agent setup built with CrewAI to simplify and automate OSINT (Open Source Intelligence) analysis of companies. This tool leverages multiple specialized AI agents to gather comprehensive intelligence across various domains including company information, website analysis, network infrastructure, social media presence, and more.

## 🚀 Features

- **Multi-Agent Architecture**: 11 specialized agents working together to provide comprehensive OSINT analysis
- **Automated Intelligence Gathering**: Collects data from multiple sources automatically
- **Comprehensive Reporting**: Generates detailed OSINT reports with structured findings
- **Parallel Processing**: Agents work asynchronously for faster analysis
- **Extensible Design**: Easy to add new agents and analysis capabilities

## 🤖 Agent Capabilities

### Core Analysis Agents

1. **Company Information Specialist**
   - Company background and overview
   - Founded date and founders
   - Headquarters location and industry classification
   - Subsidiaries information

2. **Website Analysis Agent**
   - Website structure and content analysis
   - Metadata examination
   - Technology stack identification (using BuiltWith)
   - SSL/TLS configuration assessment

3. **Domain & Network Analysis Agent**
   - WHOIS domain registration details
   - DNS records analysis (using DNSdumpster)
   - Subdomain enumeration
   - IP address mapping
   - Network services discovery (using Shodan)

4. **Social Media & Contact Specialist**
   - Social media presence mapping (LinkedIn, Facebook, Twitter, GitHub, Instagram)
   - Contact information gathering
   - Key personnel identification

5. **Search Engine Intelligence Agent**
   - Google Dorking techniques
   - Hidden file discovery (PDFs, confidential documents)
   - Recent news analysis and conclusions

6. **Business Information Specialist**
   - Financial data collection
   - Key personnel details
   - Partnership information
   - Business directory analysis (Bloomberg, Crunchbase, LinkedIn)

7. **Regulatory & Legal Specialist**
   - SEC filings and regulatory compliance
   - Legal issues identification
   - Security posture assessment
   - Email pattern analysis (using Hunter.io)

8. **Intellectual Property Agent**
   - Patent research and analysis
   - Trademark identification
   - Copyright information

9. **Employee & Hiring Intelligence**
   - Job listing analysis
   - Employee reviews (Glassdoor)
   - Hiring patterns and trends

10. **Community & Public Perception Agent**
    - Customer reviews analysis (Trustpilot, Google Reviews)
    - Forum discussions monitoring (Reddit, industry forums)
    - Public sentiment analysis

11. **OSINT Report Generator**
    - Consolidates all findings into comprehensive reports
    - Structured analysis and insights
    - Executive summary generation

## 📋 Prerequisites

- Python 3.8+
- CrewAI framework
- Exa API key for search capabilities
- IPython for report display

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/OSINT-Agent-Orchestration.git
cd OSINT-Agent-Orchestration
```

2. Install required dependencies:
```bash
pip install crewai exa-py ipython
```

3. Set up environment variables:
```bash
# Create a .env file and add your API keys
echo "EXA_API_KEY=your_exa_api_key_here" > .env
```

## 🚀 Usage

1. Run the main application:
```bash
python app.py
```

2. Enter the company name when prompted:
```
Enter the name of company
> Tesla
```

3. The system will automatically:
   - Deploy all 11 specialized agents
   - Conduct parallel analysis across different domains
   - Generate a comprehensive OSINT report
   - Display results in structured markdown format

## 📁 Project Structure

```
OSINT-Agent-Orchestration/
├── app.py                 # Main application entry point
├── agents.py             # Agent definitions and configurations
├── tasks.py              # Task definitions for each agent
├── utils.py              # Utility functions and tools (Exa search integration)
├── README.md             # Project documentation
├── .gitignore           # Git ignore rules
└── .env                 # Environment variables (not tracked)
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
EXA_API_KEY=your_exa_api_key_here
```

### Agent Customization

Each agent can be customized by modifying the `agents.py` file:

- **Role**: Define the agent's primary function
- **Goal**: Set specific objectives
- **Tools**: Assign available tools and capabilities
- **Backstory**: Provide context for better performance

### Task Configuration

Tasks are defined in `tasks.py` and can be modified to:
- Change analysis scope
- Adjust output formats
- Add new investigation areas
- Modify async execution behavior

## 🔍 Search Tools

The system uses Exa API for intelligent search capabilities:

- **Search**: Query-based web search with autoprompt
- **Find Similar**: Discover related content based on URLs
- **Get Contents**: Extract full content from web pages

## 📊 Output Format

The system generates comprehensive reports including:

- **Executive Summary**: High-level findings and key insights
- **Company Profile**: Basic company information and structure
- **Technical Analysis**: Website, domain, and network infrastructure
- **Social Intelligence**: Social media and contact information
- **Business Intelligence**: Financial data and partnerships
- **Legal & Compliance**: Regulatory filings and legal issues
- **Market Perception**: Customer reviews and public sentiment
- **Security Assessment**: Technical vulnerabilities and risks

## 🛡️ Ethical Guidelines

This tool is designed for legitimate OSINT research purposes only:

- ✅ Competitive intelligence
- ✅ Due diligence research
- ✅ Security assessments
- ✅ Academic research
- ❌ Illegal surveillance
- ❌ Harassment or stalking
- ❌ Unauthorized access attempts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewai) for the multi-agent framework
- [Exa](https://exa.ai/) for intelligent search capabilities
- Open source intelligence community for methodologies and best practices

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/OSINT-Agent-Orchestration/issues) page
2. Create a new issue with detailed description
3. Provide relevant logs and error messages

## 🔮 Future Enhancements

- [ ] Dark web monitoring capabilities
- [ ] Real-time threat intelligence feeds
- [ ] Integration with additional OSINT tools
- [ ] Web-based dashboard interface
- [ ] Export capabilities (PDF, JSON, XML)
- [ ] Automated scheduling and monitoring
- [ ] Machine learning-based anomaly detection

---

**⚠️ Disclaimer**: This tool is for educational and legitimate research purposes only. Users are responsible for ensuring compliance with applicable laws and regulations when conducting OSINT activities.