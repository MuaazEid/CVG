// Resume Generator JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips and other Bootstrap components
    initializeBootstrapComponents();
    
    // Add character counters
    addCharacterCounters();
    
    console.log('Resume Generator initialized successfully');
});

/**
 * Initialize form validation
 */
function initializeFormValidation() {
    const form = document.getElementById('resumeForm');
    if (!form) return;
    
    // Add real-time validation
    const textAreas = form.querySelectorAll('textarea');
    textAreas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            validateField(this);
        });
        
        textarea.addEventListener('blur', function() {
            validateField(this);
        });
    });
    
    // Remove ALL form event listeners - let HTML form work naturally
    console.log('Form found, but letting it submit naturally without JS interference');
}

/**
 * Validate individual form field
 */
function validateField(field) {
    const value = field.value.trim();
    const minLength = getMinLength(field.name);
    const maxLength = getMaxLength(field.name);
    
    // Remove existing validation classes
    field.classList.remove('is-valid', 'is-invalid');
    
    // Clear previous error messages
    const existingFeedback = field.parentNode.querySelector('.invalid-feedback');
    if (existingFeedback) {
        existingFeedback.style.display = 'none';
    }
    
    // Validate length
    if (value.length < minLength) {
        field.classList.add('is-invalid');
        showFieldError(field, `Please provide at least ${minLength} characters.`);
        return false;
    } else if (value.length > maxLength) {
        field.classList.add('is-invalid');
        showFieldError(field, `Please keep within ${maxLength} characters.`);
        return false;
    } else {
        field.classList.add('is-valid');
        return true;
    }
}

/**
 * Get minimum length for field
 */
function getMinLength(fieldName) {
    const minLengths = {
        'job_titles': 10,
        'projects': 10,
        'skills': 5,
        'education': 10
    };
    return minLengths[fieldName] || 10;
}

/**
 * Get maximum length for field
 */
function getMaxLength(fieldName) {
    const maxLengths = {
        'job_titles': 2000,
        'projects': 2000,
        'skills': 1000,
        'education': 1000
    };
    return maxLengths[fieldName] || 1000;
}

/**
 * Show field-specific error message
 */
function showFieldError(field, message) {
    let feedback = field.parentNode.querySelector('.invalid-feedback');
    if (!feedback) {
        feedback = document.createElement('div');
        feedback.className = 'invalid-feedback';
        field.parentNode.appendChild(feedback);
    }
    feedback.innerHTML = `<small><i class="fas fa-exclamation-triangle me-1"></i>${message}</small>`;
    feedback.style.display = 'block';
}

/**
 * Validate entire form
 */
function validateForm() {
    const form = document.getElementById('resumeForm');
    if (!form) return false;
    
    const textAreas = form.querySelectorAll('textarea');
    let isValid = true;
    
    textAreas.forEach(textarea => {
        if (!validateField(textarea)) {
            isValid = false;
        }
    });
    
    return isValid;
}

/**
 * Show validation errors summary
 */
function showValidationErrors() {
    const invalidFields = document.querySelectorAll('.is-invalid');
    if (invalidFields.length > 0) {
        // Scroll to first invalid field
        invalidFields[0].scrollIntoView({ 
            behavior: 'smooth', 
            block: 'center' 
        });
        invalidFields[0].focus();
        
        // Show error alert
        showAlert('Please correct the errors below before submitting.', 'error');
    }
}

/**
 * Initialize loading states
 */
function initializeLoadingStates() {
    const form = document.getElementById('resumeForm');
    const submitBtn = document.getElementById('submitBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');
    
    if (!form || !submitBtn || !loadingSpinner) return;
    
    form.addEventListener('submit', function() {
        if (validateForm()) {
            showLoadingState();
        }
    });
}

/**
 * Show loading state during form submission
 */
function showLoadingState() {
    const submitBtn = document.getElementById('submitBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');
    
    if (submitBtn && loadingSpinner) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-cog fa-spin me-2"></i>Generating Resume...';
        loadingSpinner.classList.remove('d-none');
        
        // DO NOT disable form inputs during submission - this prevents data from being sent
        console.log('Loading state activated, form will submit normally');
    }
}

/**
 * Initialize Bootstrap components
 */
function initializeBootstrapComponents() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
}

/**
 * Add character counters to text areas
 */
function addCharacterCounters() {
    const textAreas = document.querySelectorAll('textarea');
    
    textAreas.forEach(textarea => {
        const maxLength = getMaxLength(textarea.name);
        
        // Create counter element
        const counter = document.createElement('small');
        counter.className = 'form-text text-muted character-counter';
        counter.style.float = 'right';
        
        // Insert counter after textarea
        textarea.parentNode.insertBefore(counter, textarea.nextSibling);
        
        // Update counter function
        function updateCounter() {
            const currentLength = textarea.value.length;
            const remaining = maxLength - currentLength;
            
            counter.textContent = `${currentLength}/${maxLength}`;
            
            if (remaining < 100) {
                counter.className = 'form-text text-warning character-counter';
            } else if (remaining < 0) {
                counter.className = 'form-text text-danger character-counter';
            } else {
                counter.className = 'form-text text-muted character-counter';
            }
        }
        
        // Initial counter update
        updateCounter();
        
        // Update counter on input
        textarea.addEventListener('input', updateCounter);
    });
}

/**
 * Show alert message
 */
function showAlert(message, type = 'info') {
    const alertContainer = document.querySelector('.container');
    if (!alertContainer) return;
    
    const alertEl = document.createElement('div');
    alertEl.className = `alert alert-${type === 'error' ? 'danger' : type} alert-dismissible fade show`;
    alertEl.innerHTML = `
        <i class="fas fa-${type === 'error' ? 'exclamation-triangle' : 'info-circle'} me-2"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insert alert at top of container
    alertContainer.insertBefore(alertEl, alertContainer.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (alertEl.parentNode) {
            alertEl.remove();
        }
    }, 5000);
}

/**
 * Enhanced print functionality
 */
function enhancedPrint() {
    // Add print-specific styles
    const printStyles = `
        @media print {
            @page {
                margin: 0.5in;
                size: letter;
            }
            
            body {
                font-size: 11pt;
                line-height: 1.3;
                color: black;
            }
            
            .resume-header h1 {
                font-size: 18pt;
                color: black;
            }
            
            .section-title {
                font-size: 14pt;
                color: black;
                border-bottom: 1pt solid black;
            }
            
            .skills-tags .badge {
                border: 1pt solid black;
                color: black;
                background: white;
                padding: 2pt 4pt;
                margin: 1pt;
            }
        }
    `;
    
    const styleSheet = document.createElement('style');
    styleSheet.textContent = printStyles;
    document.head.appendChild(styleSheet);
    
    // Print
    window.print();
    
    // Remove print styles after printing
    setTimeout(() => {
        document.head.removeChild(styleSheet);
    }, 1000);
}

/**
 * Auto-save form data to localStorage
 */
function initializeAutoSave() {
    const form = document.getElementById('resumeForm');
    if (!form) return;
    
    const textAreas = form.querySelectorAll('textarea');
    
    // Load saved data and notify user
    let hasRestoredData = false;
    textAreas.forEach(textarea => {
        const savedValue = localStorage.getItem(`resume_${textarea.name}`);
        if (savedValue) {
            textarea.value = savedValue;
            hasRestoredData = true;
            console.log(`Restored data for ${textarea.name}:`, savedValue.substring(0, 100) + '...');
        }
    });
    
    if (hasRestoredData) {
        showAlert('Your previous form data has been restored from local storage.', 'info');
    }
    
    // Save data on input
    textAreas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            localStorage.setItem(`resume_${this.name}`, this.value);
            console.log(`Saved ${this.name} to localStorage`);
        });
    });
    
    // Clear saved data on successful submission
    form.addEventListener('submit', function() {
        if (validateForm()) {
            console.log('Clearing localStorage on successful submission');
            textAreas.forEach(textarea => {
                localStorage.removeItem(`resume_${textarea.name}`);
            });
        }
    });
}

/**
 * Add keyboard shortcuts
 */
function initializeKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + Enter to submit form
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            const form = document.getElementById('resumeForm');
            if (form) {
                form.submit();
            }
        }
        
        // Ctrl/Cmd + P to print (on resume page)
        if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
            const resumeContent = document.getElementById('resumeContent');
            if (resumeContent) {
                e.preventDefault();
                enhancedPrint();
            }
        }
    });
}

// Minimal initialization - no form interference  
document.addEventListener('DOMContentLoaded', function() {
    console.log('Basic Resume Generator loaded - form will work naturally');
});

/**
 * Show stored data for debugging
 */
function showStoredData() {
    const fieldNames = ['job_titles', 'projects', 'skills', 'education'];
    let storedData = [];
    
    fieldNames.forEach(fieldName => {
        const savedValue = localStorage.getItem(`resume_${fieldName}`);
        if (savedValue) {
            storedData.push(`${fieldName}: ${savedValue.substring(0, 100)}${savedValue.length > 100 ? '...' : ''}`);
        }
    });
    
    if (storedData.length > 0) {
        alert('Stored data found:\n\n' + storedData.join('\n\n'));
    } else {
        alert('No stored data found in local storage.');
    }
}

/**
 * Clear all stored data
 */
function clearStoredData() {
    if (confirm('Are you sure you want to clear all saved form data?')) {
        const fieldNames = ['job_titles', 'projects', 'skills', 'education'];
        fieldNames.forEach(fieldName => {
            localStorage.removeItem(`resume_${fieldName}`);
        });
        showAlert('All saved data has been cleared.', 'info');
        
        // Clear form fields
        const textareas = document.querySelectorAll('textarea');
        textareas.forEach(textarea => {
            textarea.value = '';
        });
    }
}

// Export functions for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        validateField,
        validateForm,
        getMinLength,
        getMaxLength,
        showStoredData,
        clearStoredData
    };
}
